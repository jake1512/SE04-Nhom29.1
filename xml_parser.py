import xml.etree.ElementTree as ET

def get_xml_data(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    name = dict()
    W = dict()
    D = dict()
    H = dict()
    PX, PY = dict(), dict()
    posXY = dict()

    for part in root.iter('Part'):
        # print(part.attrib)
        id = part.get('ID')
        key = id
        name[key] = part.get('name')
        for value in part.iter('Values'):
            W[key] = (float) (value.find('W').text)
            D[key] = (float) (value.find('D').text)
            H[key] = (float) (value.find('H').text)
            PX[key] = (float) (value.find('PX').text)
            PY[key] = (float) (value.find('PY').text)
            
        posxy = []
        for pointdef in part.iter('PointDef'):
            x = (float) (pointdef.get('posX'))
            y = (float) (pointdef.get('posY'))
            posxy.append((x, y))
        posXY[key] = posxy
    return name, W, D, H, PX, PY, posXY