import re

def regex_extract():
    text = 'select a.uid,b.uname from (Select * from user ) a, (select * from user_details) b'
    tbl=[]
    col=[]
    als=[]
    
    
    # Extracting Columns
    cols = re.findall('Select(.+?)from', text.replace('*',''),re.IGNORECASE)
    if cols:
        trxcol1 = "".join([col.strip() for col in cols if col.strip()])
        trxcol2 = [i for i in trxcol1.split(',')]
        res = [i.split('.')[1] for i in trxcol2]
    
    
    # Extracting tables
    splitQry =text.split(' ')  
    getTbl = [k+1 for k,v in enumerate(splitQry) if v == 'from']
    getAlias = [k+2 for k,v in enumerate(splitQry) if v == 'from']
    
    for i in getTbl:
        if not re.search("\(",splitQry[i]):
            tbl.append(splitQry[i].replace(')',''))
            
    return list(zip(res,tbl))
  

regex_extract()

