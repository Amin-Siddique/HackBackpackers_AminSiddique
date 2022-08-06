def get_NullToValue(val1,val2):
  '''
  val1 : input parameter could be expression.
  val2 : input parameter to return as output if val1 evaluates to NULL
  return is Boolean
  '''
  return iifNull(val1,val2)
  
  
 ##example:
##get_NullToValue(null,20)
#output:  20

##get_NullToValue('azure','data')
#output:  azure
