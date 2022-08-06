def get_curr_ts:
  vdate = toDate(currentTimestamp())
  vhour = hour(currentTimestamp())
  vmin = minute(currentTimestamp())
  vsec = second(currentTimestamp())
  adf_curr_Ts_func = concat(toString(vdate),' ',toString(vhour),':',toString(vmin),':',toString(vsec))
  return adf_curr_Ts_func
