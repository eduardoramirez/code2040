import httplib
import json

conn = httplib.HTTPConnection('challenge.code2040.org')

headers = {'Content-type': 'application/json'}

token = json.dumps({'token': 'ixcbULz7mT'})

conn.request('POST', '/api/status', token, headers)

res = conn.getresponse()

ret  = json.loads(res.read())

print ret