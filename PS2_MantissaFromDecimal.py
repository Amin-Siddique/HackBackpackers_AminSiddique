def get_MantissaFromDecimal(val):
  '''
  val : input parameter as decimal
  '''
  convert_to_string = toString(val)
  v_split = split(convert_to_string,'.')[2]
  return v_split
  
  
 ##example:
##get_MantissaFromDecimal('243.7675')
#output:  7675
