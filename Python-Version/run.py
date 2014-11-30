import stages
import common

info = {'email': 'edyr96@hotmail.com',
  'github': 'https://github.com/eduardoramirez/code2040'}
token = common.getToken(info)

# run problem 1
print "Running Stage I..."

string = common.getData('/api/getstring', token)['result']
reverse = stages.stageI(string)
common.sendData('/api/validatestring', token, ('string', reverse))

#run problem 2
print "Running Stage II..."

info = common.getData('/api/haystack', token)['result']
needle = info['needle']
haystack = info['haystack']
index = stages.stageII(needle, haystack)
common.sendData('/api/validateneedle', token, ('needle', index))

# run problem 3
print "Running Stage III..."

info = common.getData('/api/prefix', token)['result']
prefix = info['prefix']
strings = info['array']
newStrings = stages.stageIII(prefix, strings)
common.sendData('/api/validateprefix', token, ('array', newStrings))

#run part 4
print "Running Stage IV..."

info = common.getData('/api/time', token)['result']
interval = info['interval']
date = info['datestamp']
newDate = stages.stageIV(interval, date)
common.sendData('/api/validatetime', token, ('datestamp', newDate))