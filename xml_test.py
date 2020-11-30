import xml.etree.ElementTree as ET

tree = ET.parse('.data.xml')
root = tree.getroot()
print(root)

for part in root.iter('Part'):
    name = part.get('name')
    print(name)
    for value in part.iter('Values'):
        W = value.find('W').text
        D = value.find('D').text
        H = value.find('H').text
        PX = value.find('PX').text
        PY = value.find('PY').text
        PZ = value.find('PZ').text
        RX = value.find('RZ').text
        RY = value.find('RY').text
        RZ = value.find('RZ').text
        print(W, D, H, PX, PY, PZ, RX, RY, RZ)
        for pointdef in part.iter('PointDef'):
            posX = pointdef.get('posX')
            posY = pointdef.get('posY')
            print('posX = %s' %posX, 'posY = %s' %posY)
                