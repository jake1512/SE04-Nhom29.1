import ezdxf

def test(fmt):
    doc = ezdxf.new('R2018', setup=('linetypes', 'styles'))
    msp = doc.modelspace()
    ezdxf.setup_dimstyle(doc, fmt)

    
    # Big rect
    rect1 = ([
        (150, 100),
        (800, 100),
        (800, 650),
        (150, 650),
        (150, 100),
    ])

    msp.add_lwpolyline(rect1)

    # Small rect
    rect2 = ([
        (1000, 100),
        (1030, 100),
        (1030, 650),
        (1000, 650),
        (1000, 100),
    ])

    msp.add_lwpolyline(rect2)

    dimh1 = msp.add_linear_dim(
        base=(950, 760), p1=(150, 760), p2=(800, 760),
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimh1.set_arrows(blk="OPEN90")
    dimh1.render()

    dimh21 = msp.add_linear_dim(
        base=(313, 710), p1=(150, 710), p2=(163, 710),
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimh21.set_location(location=(30, 35), leader=True, relative=True)
    dimh21.set_arrows(blk="OPEN90")
    dimh21.render()

    dimh22 = msp.add_linear_dim(
        base=(637, 710), p1=(163, 710), p2=(800, 710),
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimh22.set_arrows(blk="OPEN90")
    dimh22.render()

    dimv1 = msp.add_linear_dim(
        base=(50, 750), p1=(50, 100), p2=(50, 650), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimv1.set_arrows(blk="OPEN90")
    dimv1.render()

    dimv2 = msp.add_linear_dim(
        base=(100, 750), p1=(100, 100), p2=(100, 625), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimv2.set_arrows(blk="OPEN90")
    dimv2.render()

    dimv3 = msp.add_linear_dim(
        base=(100, 1275), p1=(100, 625), p2=(100, 650), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimv3.set_arrows(blk="OPEN90")
    dimv3.render()

    dimv4 = msp.add_linear_dim(
        base=(950, 750), p1=(950, 100), p2=(950, 625), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        }
    )
    dimv4.set_arrows(blk="OPEN90")
    dimv4.render()

    dimv5 = msp.add_linear_dim(
        base=(950, 25), p1=(950, 625), p2=(950, 650), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimasz':5,
        
        }
    )
    dimv5.set_arrows(blk="OPEN90")
    dimv5.render()

    doc.saveas('demo5.dxf')

test('EZ_CM_100_H15_CM')