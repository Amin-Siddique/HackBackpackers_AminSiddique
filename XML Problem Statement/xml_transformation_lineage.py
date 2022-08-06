url='https://raw.githubusercontent.com/Amin-Siddique/HackBackpackers_AminSiddique/main/importing_xml.xml'

import requests,xml.etree.ElementTree as ET
res = requests.get(url)

with open('ps3.xml', 'wb') as f:
        f.write(res.content)

# create element tree object
tree = ET.parse('ps3.xml')
  
# get root element
root = tree.getroot()



##creating top lineage
def get_col_lineage():
        t1 = []
        for x in root[0][0][0][0]:  ##going to TRANSFORMFIELD tag
                try:
                        t1 += [(x.attrib['NAME'] + '------->' + x.attrib['EXPRESSION'])]
                except:
                        t1 += [(x.attrib['NAME'] + '------->' + 'None')]
                        pass

         for x in root[0][0][0][1]:
                try:
                        t1 += [(x.attrib['NAME'] + '------->' + x.attrib['EXPRESSION'])]
                except:
                        t1 += [(x.attrib['NAME'] + '------->' + 'None')]
                        pass
return t1

get_col_lineage()
