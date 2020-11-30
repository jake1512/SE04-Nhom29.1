import ezdxf

def _rect(PX, PY):
    rect = ([
        (PX + 0, PY + 0),
        (PX + 0, PY + 550),
        (PX + 650, PY + 550),
        (PX + 650, PY + 0),
        (PX + 0, PY + 0),
    ])
    return rect

def _rot_rect(PX, PY):
    rect = ([
        (PX + 100 + 650, PY + 0),
        (PX + 100 + 650, PY + 550),
        (PX + 100 + 650 + 18, PY + 550),
        (PX + 100 + 650 + 18, PY + 0), 
        (PX + 100 + 650, PY + 0),
    ])
    return rect

def make_dim(p1, p2, distance):
    dim = msp.add_aligned_dim(
        p1=p1, p2=p2, distance=distance, 
        override={
            'dimclrd': 1, 
            'dimclre': 1, 
            'dimtad': 0, 
            'dimfxlon': 1, 
            'dimexe': 7, 
            'dimfxl': 7, 
            'dimtxt': 15,
            'dimlfac': 1,
            }
        )
    dim.set_arrows(blk='OPEN90', size=6.0)
    dim.render()
    return dim
    

doc = ezdxf.new('R2018', setup=True)
msp = doc.modelspace()
msp.add_lwpolyline(_rect(400, 0))
msp.add_lwpolyline(_rot_rect(400, 0))
make_dim(p1=(400, 550), p2=(1050, 550), distance=30)
make_dim(p1=(400, 0), p2=(400, 550), distance=30)
make_dim(p1=(1150, 0), p2=(1150, 550), distance=30)
doc.saveas('test_xml_rect.dxf')
