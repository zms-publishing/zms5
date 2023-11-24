from Products.zms import standard
import json
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
# import pdb

def manage_opensearch_init( self):

  resp_text = '//RESPONSE\n'
  url = self.getConfProperty('opensearch.url')
  username = self.getConfProperty('opensearch.username', 'admin')
  password = self.getConfProperty('opensearch.password', 'admin')
  schema = self.getConfProperty('opensearch.schema','{}')
  verify = bool(self.getConfProperty('opensearch.ssl.verify', ''))
  auth = HTTPBasicAuth(username,password)
  headers = {'Content-type': 'application/x-ndjson'}
  # pdb.set_trace()
  root_id = self.getRootElement().getHome().id

  try:
    resp_text += 'PUT %s\n'%('%s/%s'%(url,root_id))
    response = requests.put('%s/%s'%(url,root_id),auth=auth,headers=headers,json=schema,verify=verify)
    resp_text += json.dumps(response.json(), separators=(",", ":"), indent=2)
    response.raise_for_status()
  except:
    resp_text += '\n\n'
    resp_text += '//ERROR\n'
    resp_text += standard.writeError(self,'Error: %s'%(resp_text))
  
  # concatinate opensearch response and schema
  resp_text += '\n\n'
  resp_text += '//SCHEMA\n'
  resp_text += schema

  return resp_text