import httplib
import json

conn = httplib.HTTPConnection('challenge.code2040.org')

headers = {'Content-type': 'application/json'}

token = json.dumps({'token': 'ixcbULz7mT'})

conn.request('POST', '/api/prefix', token, headers)

res = conn.getresponse()

ret  = json.loads(res.read().decode()).values()[0].values()

prefix = ret[1]

strings = ret[0]

toReturn = []

for s in strings:
  if not s.startswith(prefix):
    toReturn.append(s)

answer = json.dumps({'token': 'ixcbULz7mT', 'array' : toReturn})

conn.request('POST', '/api/validateprefix', answer, headers)
