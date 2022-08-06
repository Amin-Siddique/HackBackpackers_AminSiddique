def get_Str(val,num):
  '''
  val : input parameter as string.
  num : number of times
  return is Boolean
  '''
  v_tf = rpad(val,length(val)*num,val)
  return v_tf
  
  
 ##example:
##get_Field('choc',5)
#output:  chocchocchocchocchoc
