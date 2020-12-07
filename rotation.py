import math


# 3D rotation
def rotateZ3D(theta, posxy):
    sinTheta = math.sin(math.radians(theta))
    cosTheta = math.cos(math.radians(theta))
    
    newPosXY = []
    for node in posxy:
        tmpx = node[0]
        tmpy = node[1]
        x = tmpx * cosTheta - tmpy * sinTheta
        y = tmpy * cosTheta + tmpx * sinTheta
        newPosXY.append((x, y, node[2]))
    return newPosXY

def rotateX3D(theta, posxy):
    sinTheta = math.sin(math.radians(theta))
    cosTheta = math.cos(math.radians(theta))
    
    newPosXY = []
    for node in posxy:
        tmpz = node[2]
        tmpy = node[1]
        z = tmpz * cosTheta + tmpy * sinTheta
        y = tmpy * cosTheta - tmpz * sinTheta
        newPosXY.append((node[0], y, z))
    return newPosXY

def rotateY3D(theta, posxy):
    sinTheta = math.sin(math.radians(theta))
    cosTheta = math.cos(math.radians(theta))
    
    newPosXY = []
    for node in posxy:
        tmpx = node[0]
        tmpz = node[2]
        x = tmpx * cosTheta + tmpz * sinTheta
        z = tmpz * cosTheta - tmpx * sinTheta
        newPosXY.append((x, node[1], z))
    return newPosXY

def rotate3D(rx, ry, rz, posxy, h):
    newPosXY = []
    for node in posxy:
        newPosXY.append((node[0], node[1], h))
    posxy = newPosXY
    if rx != 0:
        posxy = rotateX3D(rx, posxy)
    if ry != 0:
        posxy = rotateY3D(ry, posxy)
    if rz != 0:
        posxy = rotateZ3D(rz, posxy)
    return posxy