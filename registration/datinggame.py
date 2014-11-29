import httplib
import json
from datetime import datetime, timedelta
from dateutil import parser

conn = httplib.HTTPConnection('challenge.code2040.org')

headers = {'Content-type': 'application/json'}

token = json.dumps({'token': 'ixcbULz7mT'})

conn.request('POST', '/api/time', token, headers)

res = conn.getresponse()

ret  = json.loads(res.read().decode()).values()[0].values()

interval = ret[1]

date = ret[0]


time = parser.parse(date)

ti = time + timedelta(seconds=interval)

toReturn =  ti.isoformat()

answer = json.dumps({'token': 'ixcbULz7mT', 'datestamp' : toReturn})

conn.request('POST', '/api/validatetime', answer, headers)