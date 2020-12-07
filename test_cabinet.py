from logging import disable
import ezdxf
from ezdxf.entities import point
from xml_parser import get_xml_data
from rotation import rotate3D

from ezdxf.math.vector import distance

doc = ezdxf.new()
msp = doc.modelspace()

# get data from data.xml file
W , D, H, PX, PY, PZ, RX, RY, RZ, posXY = get_xml_data('./data.xml')

keys = ['000', '001', '002', '003', '004', '005', '006', '007', '008']

my_line_types = [
    ('DASHED1', 'DASHED - - - - - - - - - ', [8.0, 5.0, -3.0])
]
doc.linetypes.new('DASHED1', dxfattribs={'pattern' : [8.0, 5.0, -3.0]})


        
def make_dims(p1, p2, distance):
    dim = msp.add_aligned_dim(p1=p1, p2=p2, distance=distance, override={'dimclrd' : 1, 'dimclre' : 1, 'dimtad' : 0, 'dimfxlon' : 1, 'dimexe' : 7, 'dimfxl' : 7, 'dimtxt' : 14})
    dim.set_arrows(blk='OPEN90', size=6.0)
    dim.render()
    return dim
            
def drawing(key, w, d, h, px, py, pz, rx, ry, rz, posxy):
    posxy = rotate3D(rx, ry, rz, posxy, h)
    elevational_view_points = [posxy[0], posxy[1], posxy[2], posxy[3]]
    elevational_face = [[0, 1, 2, 3]]
    print(posxy[0])
    print(posxy[1])
    print(posxy[2])
    print(posxy[3])
    
    # side_view_points = [(0, 0), (0, d), (h, d), (h, 0), (0, 0)]
    
    elevational_view = doc.blocks.new(name = 'elevational_view_' + key)
    # side_view = doc.blocks.new(name = 'side_view_' + key)
    #elevational_view.add_lwpolyline(elevational_view_points)
    mesh = elevational_view.add_mesh()
    with mesh.edit_data() as mesh_data:
        mesh_data.vertices = elevational_view_points
        mesh_data.faces = elevational_face
    # side_view.add_lwpolyline(side_view_points)
    msp.add_blockref('elevational_view_' + key, (px, py, pz))
    # msp.add_blockref('side_view_' + key, (px + w + 30, py, pz))
    # make_dims((px, py), (px, py + d), distance=30)
    # make_dims((px, py + d), (px + w, py + d), distance=30)
    
for key in keys:
    drawing(key, W[key], D[key], H[key], PX[key], PY[key], PZ[key], RX[key], RY[key], RZ[key], posXY[key])
    


# left_open_cabinet = doc.blocks.new(name='left_open_cabinet')
# left_open_cabinet.add_lwpolyline(points=[(0, 0), (0, 550), (650, 550), (650, 0), (0, 0)])
# msp.add_blockref('left_open_cabinet', (-325.07, 1840, 100), dxfattribs={})

# left_board = doc.blocks.new(name='left_board')
# left_board.add_lwpolyline(points=[(0, 0), (0, 550), (650, 550), (650, 0), (0, 0)])
# left_board_hcc = doc.blocks.new(name='left_board_hcc')
# left_board_hcc.add_lwpolyline([(0, 0), (18, 0), (18, 550), (0, 550), (0, 0)])
# msp.add_blockref('left_board_hcc', (598, 0, 0))
# msp.add_blockref('left_board', (18, 0, 0))

doc.saveas('test_cabinet.dxf')