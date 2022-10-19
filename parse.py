import xml.etree.ElementTree as et
tr=et.parse('testSample.xml')
myroot=tr.getroot()

for x in myroot.findall('food'):
    item =x.find('item').attrib
    if item['name']=='breakfast':
        print(x.find('item').text)