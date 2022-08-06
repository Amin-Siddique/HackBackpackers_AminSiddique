def get_RawLength(val):
  '''
  val : input parameter could be any.
  '''
  return toByte(length(toString(toBinary(val))))
  
  
 ##example:
##get_RawLength('abcd')
#output:  4
