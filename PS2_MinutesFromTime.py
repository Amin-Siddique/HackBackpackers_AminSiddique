def get_minsFromTime(time):
  '''
  time - Input parameter in the form HH:mm:ss
  return type - Integer
  '''
  v_ts = toTimestamp('time','HH:mm:ss')
  v_getmins = minute(v_ts)
  return v_getmins

#example:
# expression =>  minute(toTimestamp('22:30:52','HH:mm:ss'))
# output => 30
