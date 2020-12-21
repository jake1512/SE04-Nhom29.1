import ezdxf
from xml_parser import get_xml_data


doc = ezdxf.new()
msp = doc.modelspace()

# get data from data.xml file
W , D, H, PX, PY, PZ, RX, RY, RZ, posXY = get_xml_data('./data.xml')

# set keys
keys = ['000', '001', '002', '003', '004', '005', '006', '007', '008']
        
def make_dims(p1, p2, distance):
    dim = msp.add_aligned_dim(p1=p1, p2=p2, distance=distance, override={'dimclrd' : 1, 'dimclre' : 1, 'dimtad' : 0, 'dimfxlon' : 1, 'dimexe' : 7, 'dimfxl' : 7, 'dimtxt' : 14})
    dim.set_arrows(blk='OPEN90', size=6.0)
    dim.render()
    return dim
            
def drawing(key, w, d, h, px, py, pz, posxy):
    elevational_view_points = [posxy[0], posxy[1], posxy[2], posxy[3], posxy[0]]
    side_view_points = [(0, 0), (0, d), (h, d), (h, 0), (0, 0)]
    
    elevational_view = doc.blocks.new(name = 'elevational_view_' + key)
    side_view = doc.blocks.new(name = 'side_view_' + key)
    elevational_view.add_lwpolyline(elevational_view_points)
    side_view.add_lwpolyline(side_view_points)
    msp.add_blockref('elevational_view_' + key, (px, py))
    msp.add_blockref('side_view_' + key, (px + w + 75, py))
    make_dims((px, py), (px, py + d), distance=30)
    make_dims((px, py + d), (px + w, py + d), distance=30)
    make_dims((px + w + 75, py), (px + w + 75, py + d), distance=30)
    
drawing(keys[1], W[keys[1]], D[keys[1]], H[keys[1]], -900, 0, PZ[keys[1]], posXY[keys[1]])
drawing(keys[2], W[keys[2]], D[keys[2]], H[keys[2]], 800, 0, PZ[keys[2]], posXY[keys[2]])
drawing(keys[3], W[keys[3]], D[keys[3]], H[keys[3]], 0, 0, PZ[keys[3]], posXY[keys[3]])
drawing(keys[4], W[keys[4]], D[keys[4]], H[keys[4]], 1700, 0, PZ[keys[4]], posXY[keys[4]])
drawing(keys[5], W[keys[5]], D[keys[5]], H[keys[5]], 2600, 0, PZ[keys[5]], posXY[keys[5]])
drawing(keys[6], W[keys[6]], D[keys[6]], H[keys[6]], 3000, 0, PZ[keys[6]], posXY[keys[6]])
drawing(keys[7], W[keys[7]], D[keys[7]], H[keys[7]], 3700, 0, PZ[keys[7]], posXY[keys[7]])
# drawing(keys[8], W[keys[8]], D[keys[8]], H[keys[8]], PX[keys[8]], 0, PZ[keys[8]], posXY[keys[8]])
    

doc.saveas('test_cabinet.dxf')