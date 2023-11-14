id = 'zcatalog_interface'
from Products.zms import standard

def getZCatalog(context, lang):
  cat_id = 'catalog_%s'%lang
  root = context.getRootElement()
  return getattr(root, cat_id, None)

def catalog_object(zcatalog, adapter, node, data):
  attr_ids = adapter._getAttrIds()
  # Prepare object.
  for attr_id in attr_ids:
    attr_name = 'zcat_index_%s'%attr_id
    value = data.get(attr_id)
    if value == 'None':
      value = None
    setattr(node, attr_name, value)
  # (Re-)Catalog object.
  path = node.getPath()
  if zcatalog.getrid(path):
    zcatalog.uncatalog_object(path)
  zcatalog.catalog_object(node, path)
  # Unprepare object.
  for attr_id in attr_ids:
    attr_name = 'zcat_index_%s'%attr_id
    delattr(node, attr_name)

def manage_zcatalog_object_add( self, node, data):
  request = self.REQUEST
  lang = standard.nvl(request.get('lang'), self.getPrimaryLanguage())
  if 'ZMS_ENV_ZCATALOG' not in request:
    request['ZMS_ENV_ZCATALOG'] = getZCatalog(self, lang)
  zcatalog = request['ZMS_ENV_ZCATALOG']
  adapter = self.getCatalogAdapter()
  catalog_object(zcatalog, adapter, node, data)
  return 1
