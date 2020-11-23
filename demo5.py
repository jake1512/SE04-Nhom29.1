import ezdxf

def test(fmt):
    doc = ezdxf.new('R2018', setup=('linetypes', 'styles'))
    msp = doc.modelspace()
    ezdxf.setup_dimstyle(doc, fmt)

    

    dimh1 = msp.add_linear_dim(
        base=(950, 760), p1=(150, 760), p2=(800, 760),
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        'dimexo':42,
        }
    )
    dimh1.set_arrows(blk="")
    dimh1.render()

    dimh21 = msp.add_linear_dim(
        base=(13, 710), p1=(150, 710), p2=(163, 710),
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        'dimexo':42,
        }
    )
    dimh21.set_arrows(blk="")
    dimh21.render()

    dimh22 = msp.add_linear_dim(
        base=(963, 710), p1=(163, 710), p2=(800, 710),
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        }
    )
    dimh22.set_arrows(blk="")
    dimh22.render()

    dimv1 = msp.add_linear_dim(
        base=(50, 750), p1=(50, 100), p2=(50, 650), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        }
    )
    dimv1.set_arrows(blk="")
    dimv1.render()

    dimv2 = msp.add_linear_dim(
        base=(100, 750), p1=(100, 100), p2=(100, 625), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        }
    )
    dimv2.set_arrows(blk="")
    dimv2.render()

    dimv3 = msp.add_linear_dim(
        base=(100, 1275), p1=(100, 625), p2=(100, 650), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        }
    )
    dimv3.set_arrows(blk="")
    dimv3.render()

    dimv4 = msp.add_linear_dim(
        base=(850, 750), p1=(850, 100), p2=(850, 625), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        }
    )
    dimv4.set_arrows(blk="")
    dimv4.render()

    dimv5 = msp.add_linear_dim(
        base=(850, 1275), p1=(850, 625), p2=(850, 650), angle=90,
        dimstyle=fmt,
        override={
        'dimtad':0,
        'dimclrd':1,
        'dimblk':5,
        }
    )
    dimv5.set_arrows(blk="")
    dimv5.render()

    doc.saveas('demo5.dxf')

test('EZ_CM_100_H15_CM')