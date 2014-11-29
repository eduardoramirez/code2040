import httplib
import json

conn = httplib.HTTPConnection('challenge.code2040.org')
headers = {'Content-type': 'application/json'}

def getToken(data):
  regInfo = json.dumps(data)
  conn.request('POST', '/api/register', regInfo, headers)
  res = conn.getresponse()
  return json.loads(res.read()).values()[0]

def getData(path, token):
  conn.request('POST', path, json.dumps({'token':token}), headers)
  res = conn.getresponse()
  return json.loads(res.read())

def sendData(path, token, data):
  (key, val) = data
  dataToSend = json.dumps({'token': token, key: val})
  conn.request('POST', path, dataToSend, headers)
  res = conn.getresponse()
  grade = json.loads(res.read())['result']

  if grade.startswith('PASS'):
    print 'WOOO, you passed :)'
  else:
    print 'EHHH, try again!! :('