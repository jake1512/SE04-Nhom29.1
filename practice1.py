import ezdxf
from ezdxf.addons import Importer

doc = ezdxf.new('AC1032', setup=True)
msp = doc.modelspace()

sdoc = ezdxf.readfile('./bridge.dxf')

importer = Importer(sdoc, doc)

Block1 = doc.blocks.new('Block1')

importer.import_modelspace(Block1)
    
importer.finalize()

msp.add_blockref('Block1', (450, 600), dxfattribs={
    'xscale' : 2000,
    'yscale' : 2000
})

my_line_types = [
    ('DASHED1', 'DASHED - - - - - - - - - ', [8.0, 5.0, -3.0])
]

doc.linetypes.new('DASHED1', dxfattribs={'pattern' : [8.0, 5.0, -3.0]})

rect1_points = [(0, 0), (25, 0), (25, 550), (0, 550), (0, 0)]
rect2_points = [(125, 0), (775, 0), (775, 550), (125, 550), (125, 0)]
rect3_points = [(850, 0), (875, 0), (875, 550), (850, 550), (850, 0)]
rect4_points = [(775, 525), (138, 525), (138, 515), (775, 515)]

msp.add_lwpolyline(rect1_points)
msp.add_lwpolyline(rect2_points)
msp.add_lwpolyline(rect3_points)
msp.add_lwpolyline(rect4_points, dxfattribs={'linetype' : 'DASHED1'})

def make_dims(p1, p2, distance):
    dim = msp.add_aligned_dim(p1=p1, p2=p2, distance=distance, override={'dimclrd' : 1, 'dimclre' : 1, 'dimtad' : 0, 'dimfxlon' : 1, 'dimexe' : 7, 'dimfxl' : 7, 'dimtxt' : 14})
    dim.set_arrows(blk='OPEN90', size=6.0)
    dim.render()
    return dim

# dim1 = msp.add_aligned_dim(p1=(125, 0), p2=(125, 550), distance=30, override={'dimclrd' : 1, 'dimtad' : 0, 'dimfxlon' : 1, 'dimexe' : 10, 'dimfxl' : 10, 'dimtxt' : 14})
# dim1.set_arrows(blk="OPEN30", size=20.0)
# dim1.render()

# dim2 = msp.add_aligned_dim(p1=(125, 0), p2=(125, 550), distance=50, override={'dimclrd' : 1, 'dimtad' : 0, 'dimfxlon' : 1, 'dimexe' : 10, 'dimfxl' : 10, 'dimtxt' : 14})
# dim2.set_arrows(blk='OPEN30', size=20.0)
# dim2.render()

dim1 = make_dims(p1=(125, 0), p2=(125, 550), distance=30)
dim2 = make_dims(p1=(125, 0), p2=(125, 550), distance=60)
dim3 = make_dims(p1=(138, 525), p2=(775, 525), distance=75)
dim4 = make_dims(p1=(125, 550), p2=(775, 550), distance=80)
dim5 = make_dims(p1=(850, 0), p2=(850, 550), distance=20)
# dim6 = make_dims(p1=(125, 525), p2=(138, 525), distance=75)
dim6 = msp.add_aligned_dim(p1=(125, 525), p2=(138, 525), distance=75, override={'dimclrd' : 1, 'dimclre' : 1,'dimfxlon' : 1, 'dimexe' : 10, 'dimfxl' : 10, 'dimexe' : 7, 'dimfxl' : 7,'dimtxt' : 10})
dim6.set_arrows(blk="OPEN90", size=6.0)
dim6.set_location((25, 25), leader=True, relative=True)
dim6.render()

doc.saveas("practice1.dxf")