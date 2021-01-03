import ezdxf
from xml_parser import get_xml_data
from ezdxf.math import Vec2

# Create new .dxf file and its modelspace
doc = ezdxf.new()
msp = doc.modelspace()

# get data from data.xml file
name, W, D, H, PX, PY, posXY = get_xml_data('./data.xml')

# set keys
keys = ['000', '001', '002', '003', '004', '005', '006', '007', '008']

# create dimensions for the parts        
def make_dims(p1, p2, distance):
    dim = msp.add_aligned_dim(p1=p1, p2=p2, distance=distance, 
                            override={
                                'dimclrd' : 1,  # Dimension line, arrowhead, and leader line color
                                'dimclre' : 1,  # Dimension extension line color
                                'dimtad' : 0,   # Sets vertical text placement relative to dimension line
                                'dimfxlon' : 1, # Extension line has fixed length if set to 1
                                'dimfxl' : 7,   # Length of extension line below dimension line if fixed
                                'dimexe' : 7,   # Extension line distance beyond dimension line
                                'dimtxt' : 14,  # Size of dimension text
                                })
    dim.set_arrows(blk='OPEN90', size=6.0)      # Set arrow block type and size
    dim.render()
    return dim

# draw parts
def drawing(key, name, w, d, h, px, py, pz, posxy):
    # Set (X, Y) points
    elevational_view_points = [posxy[0], posxy[1], posxy[2], (posxy[3][0], posxy[3][1], 1.5, 1.5), posxy[0]]
    side_view_points = [(0, 0), (0, d), (h, d), (h, 0), (0, 0)]
    
    # Create blocks(containers)
    elevational_view = doc.blocks.new(name = 'elevational_view_' + key)
    side_view = doc.blocks.new(name = 'side_view_' + key)
    
    # Add points
    elevational_view.add_lwpolyline(elevational_view_points)
    side_view.add_lwpolyline(side_view_points)
    
    # Add blocks to modelspace
    msp.add_blockref('elevational_view_' + key, (px, py))
    msp.add_blockref('side_view_' + key, (px + w + 100, py))

    # Draw dimensions for the part
    make_dims((px, py), (px, py + d), distance=40)
    make_dims((px, py + d), (px + w, py + d), distance=40)
    make_dims((px + w + 100, py), (px + w + 100, py + d), distance=30)
    
    # Add name tag
    msp.add_mtext(name, dxfattribs={
                                'char_height': 24,
                                'style': 'Calibri',
                                }).set_location(insert=(px + 30, -40))
    # Small triangles
    draw_triangle(px, py, w, d)        

# Create triangle entity
def single_triangle(pos, rotation, fill):
    if not hasattr(single_triangle, "counter"):
        single_triangle.counter = 0
    single_triangle.counter += 1
    
    block_name = "triangle" + str(single_triangle.counter)
    shape_test = doc.blocks.new(name = block_name)
    points = [Vec2.from_deg_angle((360 / 3) * n) for n in range(3)]
    points.append(points[0])
    if(fill):
        hatch = shape_test.add_hatch(color = 1)
        hatch.paths.add_polyline_path(points)
    else:
        points.append(points[0])
        shape_test.add_lwpolyline(points, dxfattribs={'color' : 1})
    
    msp.add_blockref(block_name, pos, dxfattribs={'rotation' : rotation, 'xscale' : 9, 'yscale' : 9})

# Function for drawing triangles
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

# Part placement
px, py = -900, 0
for tmp in range(1, 8):
    drawing(keys[tmp], name[keys[tmp]], W[keys[tmp]], D[keys[tmp]], H[keys[tmp]], px, py, posXY[keys[tmp]])
    px += W[keys[tmp]] + 250

# Save dxf file
doc.saveas('cabinet.dxf')