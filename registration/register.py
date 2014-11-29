import httplib
import json

conn = httplib.HTTPConnection('challenge.code2040.org')

headers = {'Content-type': 'application/json'}

registrationInfo = json.dumps({'email': 'edyr96@hotmail.com',
  'github': 'https://github.com/eduardoramirez/code2040'})

conn.request('POST', '/api/register', registrationInfo, headers)

res = conn.getresponse()

print(res.read().decode())
