import httplib
import json

conn = httplib.HTTPConnection('challenge.code2040.org')

headers = {'Content-type': 'application/json'}

token = json.dumps({'token': 'ixcbULz7mT'})

conn.request('POST', '/api/haystack', token, headers)

res = conn.getresponse()

ret  = json.loads(res.read().decode()).values()[0].values()

needle = ret[1]

haystack = ret[0]

index = haystack.index(needle)

answer = json.dumps({'token': 'ixcbULz7mT', 'needle' : index})

conn.request('POST', '/api/validateneedle', answer, headers)
