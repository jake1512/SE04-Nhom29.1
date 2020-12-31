import ezdxf
from xml_parser import get_xml_data
from ezdxf.math import Vec2


doc = ezdxf.new()
msp = doc.modelspace()

# get data from data.xml file
name, W, D, H, PX, PY, PZ, RX, RY, RZ, posXY = get_xml_data('./data.xml')

# set keys
keys = ['000', '001', '002', '003', '004', '005', '006', '007', '008']
        
def make_dims(p1, p2, distance):
    dim = msp.add_aligned_dim(p1=p1, p2=p2, distance=distance, 
                            override={
                                'dimclrd' : 1, 
                                'dimclre' : 1, 
                                'dimtad' : 0, 
                                'dimfxlon' : 1, 
                                'dimexe' : 7, 
                                'dimfxl' : 7, 
                                'dimtxt' : 14
                                })
    dim.set_arrows(blk='OPEN90', size=6.0)
    dim.render()
    return dim
            
def drawing(key, name, w, d, h, px, py, pz, posxy):
    elevational_view_points = [posxy[0], posxy[1], posxy[2], (posxy[3][0], posxy[3][1], 1.5, 1.5), posxy[0]]
    side_view_points = [(0, 0), (0, d), (h, d), (h, 0), (0, 0)]
    
    elevational_view = doc.blocks.new(name = 'elevational_view_' + key)
    side_view = doc.blocks.new(name = 'side_view_' + key)
    elevational_view.add_lwpolyline(elevational_view_points)
    side_view.add_lwpolyline(side_view_points)
    msp.add_blockref('elevational_view_' + key, (px, py))
    msp.add_blockref('side_view_' + key, (px + w + 100, py))
    make_dims((px, py), (px, py + d), distance=40)
    make_dims((px, py + d), (px + w, py + d), distance=40)
    make_dims((px + w + 100, py), (px + w + 100, py + d), distance=30)
    msp.add_mtext(name, dxfattribs={
                                'char_height': 24,
                                'style': 'Calibri',
                                }).set_location(insert=(px + 30, -40))
    draw_triangle(px, py, w, d)        
        
        
def draw_triangle(px, py, w, d):
    pos = []
    rotation = []
    fill = []
    
    pos.append((px - 15, (py + d) / 2))
    pos.append((px + w / 2, py + d + 15))
    pos.append((px + w + 15, (py + d) / 2))
    pos.append((px + w / 2, py - 15))
    
    rotation.extend([0, -90, 180, 90])
    
    fill.extend([0, 0, 0, 1])
    
    for tmp in range(4):
        single_triangle(pos=pos[tmp], rotation=rotation[tmp], fill=fill[tmp])
    
    
    
def single_triangle(pos, rotation, fill):
    if not hasattr(single_triangle, "counter"):
        single_triangle.counter = 0  # it doesn't exist yet, so initialize it
    single_triangle.counter += 1
    
    block_name = "triangle" + str(single_triangle.counter)
    shape_test = doc.blocks.new(name = block_name)
    points = [Vec2.from_deg_angle((360 / 3) * n) for n in range(3)]
    points.append(points[0])
    # print(points)
    if(fill):
        hatch = shape_test.add_hatch(color = 1)
        hatch.paths.add_polyline_path(points)
    else:
        points.append(points[0])
        shape_test.add_lwpolyline(points, dxfattribs={'color' : 1})
    
    msp.add_blockref(block_name, pos, dxfattribs={'rotation' : rotation, 'xscale' : 9, 'yscale' : 9})


px, py = -900, 0
for tmp in range(1, 8):
    drawing(keys[tmp], name[keys[tmp]], W[keys[tmp]], D[keys[tmp]], H[keys[tmp]], px, py, PZ[keys[tmp]], posXY[keys[tmp]])
    px += W[keys[tmp]] + 250

# drawing(keys[1], name[keys[1]], W[keys[1]], D[keys[1]], H[keys[1]], -900, 0, PZ[keys[1]], posXY[keys[1]])
# drawing(keys[2], name[keys[2]], W[keys[2]], D[keys[2]], H[keys[2]], 800, 0, PZ[keys[2]], posXY[keys[2]])
# drawing(keys[3], name[keys[3]], W[keys[3]], D[keys[3]], H[keys[3]], 0, 0, PZ[keys[3]], posXY[keys[3]])
# drawing(keys[4], name[keys[4]], W[keys[4]], D[keys[4]], H[keys[4]], 1700, 0, PZ[keys[4]], posXY[keys[4]])
# drawing(keys[5], name[keys[5]], W[keys[5]], D[keys[5]], H[keys[5]], 2600, 0, PZ[keys[5]], posXY[keys[5]])
# drawing(keys[6], name[keys[6]], W[keys[6]], D[keys[6]], H[keys[6]], 3000, 0, PZ[keys[6]], posXY[keys[6]])
# drawing(keys[7], name[keys[7]], W[keys[7]], D[keys[7]], H[keys[7]], 3700, 0, PZ[keys[7]], posXY[keys[7]])
# # drawing(keys[8], name[keys[8]], W[keys[8]], D[keys[8]], H[keys[8]], 4600, 0, PZ[keys[8]], posXY[keys[8]])

doc.saveas('cabinet.dxf')