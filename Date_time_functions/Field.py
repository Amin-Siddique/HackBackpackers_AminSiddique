def get_Field(val,delimiter,num,occurence=1):
  '''
  val : input parameter as expression.
  delimiter : input parameter as string delimiter
  num : input parameter as int
  occuerence (optional): input parameter as integer
  return is Boolean
  '''
  cond_split_tx=iif(occurence>1,iif(num%2==0,substring(substringIndex(val,delimiter,num+2),num+1,num+1), 
                                    substring(substringIndex(val,delimiter,num+2),num+2,num)),split(val,delimiter)[num])
  return cond_split_tx
  
  
 ##example:
##get_Field('a,b,c,d',',',2)
#output:  b,c

##get_Field('a,b,c,d',',',2,2)
#output:  b,c

##get_Field('a,b,c,d,e',',',3,2)
#output:  d,e
