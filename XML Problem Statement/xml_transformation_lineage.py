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
t1 = []
for x in root[0][0][0][0]:
     try:
        t1 += [(x.attrib['NAME'] + '------->' + x.attrib['EXPRESSION'])]
     except:
        t1 += [(x.attrib['NAME'] + '------->' + 'None')]
        pass
print(t1)
