import common
from datetime import datetime, timedelta
from dateutil import parser

def stageI(str):
  return str[::-1]

def stageII(needle, haystack):
  try:
    index = haystack.index(needle)
  except:
    # error occurred, no needle in haystack
    print "no needle in haystack"
    return -1
  return index

def stageIII(prefix, strings):
  toReturn = []

  for s in strings:
    if not s.startswith(prefix):
      toReturn.append(s)

  return toReturn

def stageIV(interval, date):
  time = parser.parse(date)

  ti = time + timedelta(seconds=interval)

  return ti.isoformat()