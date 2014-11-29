import httplib
import json


conn = httplib.HTTPConnection('challenge.code2040.org')

headers = {'Content-type': 'application/json'}

token = json.dumps({'token': 'ixcbULz7mT'})

conn.request('POST', '/api/getstring', token, headers)

res = conn.getresponse()

ret = json.loads(res.read().decode())

stringToReverse = ret.values()[0]

reversedString = stringToReverse[::-1]

reverseData = json.dumps({'token': 'ixcbULz7mT','string' : reversedString})

conn.request('POST', '/api/validatestring', reverseData, headers)
