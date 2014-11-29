import httplib
import json

conn = httplib.HTTPConnection('challenge.code2040.org')
headers = {'Content-type': 'application/json'}

# Grab token from the server
def getToken(data):
  regInfo = json.dumps(data)
  conn.request('POST', '/api/register', regInfo, headers)
  res = conn.getresponse()
  return json.loads(res.read()).values()[0]

# Grab the data from the server and return it as a dict
def getData(path, token):
  conn.request('POST', path, json.dumps({'token':token}), headers)
  res = conn.getresponse()
  return json.loads(res.read())

# Send data and check if passed
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