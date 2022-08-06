def get_AlNum(val):
  '''
  val : input parameter could be expression.
  return is Boolean
  '''
  return iif(regexMatch(val,'^[a-zA-Z0-9]*$',true(),false())
  
  
 ##example:
##get_AlNum(12redroses)
#output:  True
             
##get_AlNum(OED_75_9*E)
#output:  False
