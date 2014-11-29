from datetime import datetime, timedelta
from dateutil import parser

# Reverse the string
def stageI(str):
  return str[::-1]

# Find index of needle in haystack list
def stageII(needle, haystack):
  try:
    index = haystack.index(needle)
  except:
    # error occurred, no needle in haystack
    print "no needle in haystack"
    return -1
  return index

# Return all elements that do not begin with prefix
def stageIII(prefix, strings):
  toReturn = []

  for s in strings:
    if not s.startswith(prefix):
      toReturn.append(s)

  return toReturn

# Add the interval to the date 
def stageIV(interval, date):
  time = parser.parse(date)

  ti = time + timedelta(seconds=interval)

  return ti.isoformat()