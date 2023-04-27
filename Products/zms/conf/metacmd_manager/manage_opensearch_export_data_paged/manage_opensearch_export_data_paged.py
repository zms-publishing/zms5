from Products.zms import standard
# import pdb

# TODO fixme in Products/zms/zmscontainerobject.py [607]
def get_next_node(self, allow_children=True):
  # children
  if allow_children:
    children = self.getChildNodes()
    if children:
      return children[0]
  # siblings
  parent  = self.getParentNode()
  if parent:
    siblings = parent.getChildNodes()
    index = siblings.index(self)
    if index < len(siblings) - 1:
      return siblings[index+1]
    # parent
    return get_next_node(parent,allow_children=False)
  # none
  return None

def traverse(data, node, meta_ids=[], page_size=100):
  count = 0
  #pdb.set_trace()
  while node and count < page_size:
    log = {'index':count,'path':'/'.join(node.getPhysicalPath())}
    if not meta_ids or node.meta_id in meta_ids:
      log['action'] = 'TODO implement here'
    data['log'].append(log)
    node = get_next_node(node)
    data['next_node'] = None if not node else '{$%s}'%node.get_uid()
    count += 1

def manage_opensearch_export_data_paged( self):
  request = self.REQUEST
  RESPONSE =  request.RESPONSE
  lang = self.getPrimaryLanguage()
  catalog = self.getZMSIndex().get_catalog()
  catalog_adapter = self.getCatalogAdapter()
  ids = catalog_adapter.getIds()
  
  uid = request.get('uid')
  if request.get('json') and uid:
    request.RESPONSE.setHeader("Content-Type","text/json")
    node = self.getLinkObj(uid)
    home_id = node.getHome().id
    import json
    data = {'pid':self.Control_Panel.process_id(),'uid':uid}
    if request.get('count'):
      path = '%s/content'%('/'.join(node.getHome().getPhysicalPath()))
      data['total'] = 0
      data['count'] = {}
      for meta_id in ids:
        r = catalog({'meta_id':meta_id}, path={'query':path})
        data['count'][meta_id] = len(r)
        data['total'] = data['total'] + len(r)
    if request.get('traverse'):
      page_size = int(request['page_size'])
      data['log'] = []
      data['next_node'] = None
      traverse(data,node,ids,page_size)
    return json.dumps(data)
  
  home_id = self.getHome().id
  prt = []
  prt.append('<!DOCTYPE html>')
  prt.append('<html lang="en">')
  prt.append(self.zmi_html_head(self,request))
  prt.append('<body class="%s">'%self.zmi_body_class(id='manage_zcatalog_export_data_paged'))
  prt.append(self.zmi_body_header(self,request))
  prt.append('<div id="zmi-tab">')
  prt.append(self.zmi_breadcrumbs(self,request))
  prt.append('<form class="form-horizontal card" name="form0" method="post" enctype="multipart/form-data">')
  prt.append('<input type="hidden" name="lang" value="%s"/>'%request['lang'])
  prt.append('<legend>Opensearch</legend>')
  prt.append('<div class="card-body">')
  prt.append('<h4>Export data paged</h4>')
  if False:
      prt.append('<div class="form-group row">')
      prt.append('<label class="col-sm-2 control-label">Objects</label>')
      prt.append('<div class="col-sm-5">')
      prt.append('<table class="table table-bordered">')
      prt.append('<caption>%s</caption>'%(home_id))
      prt.append('<tr>')
      prt.append('<th>Typ</th>')
      prt.append('<th>#</th>')
      prt.append('</tr>')
      for meta_id in ids:
          q = catalog({'path':home_id,'meta_id':meta_id})
          prt.append('<tr>')
          prt.append('<td>%s</td>'%(meta_id))
          prt.append('<td align="right">%i</td>'%(len(q)))
          prt.append('</tr>')
      prt.append('</table>')
      prt.append('</div>')
      prt.append('</div><!-- .form-group -->')
  prt.append('<div class="form-group row">')
  prt.append('<label class="col-sm-2 control-label">Page-Size</label>')
  prt.append('<div class="col-sm-5">')
  prt.append('<input class="form-control" id="page_size"  name="page_size:int" type="number" value="100">')
  prt.append('</div>')
  prt.append('</div><!-- .form-group -->')
  prt.append('<div class="form-group row">')
  prt.append('<label class="col-sm-2 control-label">Node</label>')
  prt.append('<div class="col-sm-5">')
  prt.append('<input class="form-control url-input" id="uid" name="uid" type="text" value="{$}">')
  prt.append('</div>')
  prt.append('</div><!-- .form-group -->')
  prt.append('<div class="form-group row">')
  prt.append('<label class="col-sm-2 control-label"></label>')
  prt.append('<div class="col-sm-5">')
  prt.append('<button id="start-button" class="btn btn-light">')
  prt.append('<i class="fas fa-play text-success"></i>')
  prt.append('</button>')
  prt.append('<button id="stop-button" class="btn btn-light" disabled="disabled">')
  prt.append('<i class="fas fa-stop"></i>')
  prt.append('</button>')
  prt.append('</div>')
  prt.append('</div><!-- .form-group -->')
  prt.append('<div class="form-group row">')
  prt.append('<label class="col-sm-2 control-label"></label>')
  prt.append('<div class="col-sm-5">')
  prt.append('<div id="count">')
  prt.append('</div>')
  prt.append('</div>')
  prt.append('</div><!-- .form-group -->')
  prt.append('<div class="d-none progress mx-3">')
  prt.append('<div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>')
  prt.append('</div>')
  prt.append('<div class="d-none alert alert-info" role="alert">')
  prt.append('</div>')
  btn = request.form.get('btn')
  uid = request.form.get('uid')
  page_size = request.form.get('page_size')
  if btn and uid and page_size:
    node = self.getLinkObj(uid)
    prt.append('<div class="form-group row">')
    prt.append('<label class="col-sm-2 control-label">&nbsp;</label>')
    prt.append('<div class="col-sm-10">')
    prt.append('<ul>')
    prt.extend(['<li>%s</li>'%str(x) for x in traverse(node,page_size)])
    prt.append('</ul>')
    prt.append('</div>')
    prt.append('</div>')
  
  prt.append('</div><!-- .card-body -->')
  prt.append('</form><!-- .form-horizontal -->')
  prt.append('</div><!-- #zmi-tab -->')
  prt.append(self.zmi_body_footer(self,request))
  prt.append('''
<style>
</style>
<script>
var uid = undefined;
var total = undefined;
var count = undefined;
var started = false;
var paused = false;
var stopped = false;
function start() {
    stopped = false;
    $(".progress .progress-bar").removeClass("bg-danger bg-warning bg-success");
    $("#stop-button").prop("disabled","");
    $(".progress.d-none").removeClass("d-none");
    $(".alert.alert-info").removeClass("d-none");
    $(".alert.alert-info").html('<div class="spinner-border text-primary mx-auto" role="status"><span class="sr-only">Loading...</span></div>');
    if (!started) {
      count = 0;
      started = true;
      paused = false;
      $("#start-button i").removeClass("fa-play text-success").addClass("fa-pause text-info");
      ajaxCount(ajaxTraverse);
    }
    else if (!paused) {
      paused = true;
      $("#start-button i").removeClass("fa-pause text-info").addClass("fa-play text-success");
      $(".progress .progress-bar").addClass("bg-warning");
    }
    else {
      paused = false;
      $("#start-button i").removeClass("fa-play text-success").addClass("fa-pause text-info");
      ajaxTraverse();
    }
    return false;
}
function stop() {
    started = false;
    stopped = true;
    $(".progress .progress-bar").removeClass("bg-success bg-warning bg-success");
    $("#start-button i").removeClass("fa-pause").addClass("fa-play");
    $("#stop-button").prop("disabled","disabled");
    $(".progress .progress-bar").addClass("bg-warning");
    return false;
}
function progress(i) {
  count = count + i;
  var perc = Math.floor(10.0*count*100/total)/10.0;
  // debugger;
  var log = `PROGRESS: total=${total}, count=${count}, per=${perc}`;
  console.log(log)
  $(".progress .progress-bar").css("width",perc+"%").attr({"aria-valuenow":perc,"title":count+"/"+total}).html(perc+"%");
}
function ajaxCount(cb) {
    uid = $("input[name='uid']").val();
    var params = {'json':true,'count':true,'uid':uid};
    $.get('manage_opensearch_export_data_paged',params,function(data) {
        total = data['total'];
        var html = '';
        html += '<table class="table table-bordered">';
        Object.entries(data['count']).forEach((k,v) => {
          html += '<tr class="' + k[0] + '">';
          html += '<td class="id">' + k[0] + '</td>';
          html += '<td class="total">' + k[1] + '</td>';
          html += '<td class="count">' + 0 + '</td>';
          html += '</tr>';
        });
        html += '</table>';
        $("#count").html(html);
        progress(0);
        cb();
    });
}
function ajaxTraverse() {
    var page_size = $("input#page_size").val();
    var params = {'json':true,'traverse':true,'uid':uid,'page_size':page_size};
    $.get('manage_opensearch_export_data_paged',params,function(data) {
        $(".alert.alert-info").html($('<pre/>',{text:JSON.stringify(data,null,2)}))
        if (!stopped && !paused) {
          uid = data['next_node'];
          progress(data['log'].filter(x => x['action']).length);
          if (uid) {
            ajaxTraverse();
          }
          else {
            stop();
            $(".progress .progress-bar").addClass("bg-success")
          }
        }
    });
}
$(function() {
  $("#start-button").click(start);
  $("#stop-button").click(stop);
});
</script>
  ''')
  prt.append('</body>')
  prt.append('</html>')
  
  return '\n'.join(prt)