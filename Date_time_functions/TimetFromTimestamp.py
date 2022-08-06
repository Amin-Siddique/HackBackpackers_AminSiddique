
def get_TimetFromTimestamp(ts_val):
  '''
  ts_val = input parameter expecting a timestamp
  '''
	v_fixed_ts = '1970-01-01 00:00:00'
  v_get_ts_diff = minus(ToTimeStamp(toString(ts_val),'yyyy-MM-dd HH:mm:ss'),ToTimeStamp(v_fixed_ts,'yyyy-MM-dd HH:mm:ss'))
  v_get_10_digits = left(toString(v_get_ts_diff),10)
  return v_get_10_digits


# example:
# get_TimetFromTimestamp('2009-02-13 23:31:30')
# output=> 1234567890
