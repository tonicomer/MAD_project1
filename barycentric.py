import numpy as np

def get_barycentric_coordinates(triangle_coordinates:np.array, point_coordinates:np.ndarray)->np.ndarray:
    A = triangle_coordinates[:,0]
    B = triangle_coordinates[:,1]
    C = triangle_coordinates[:,2]
    P = point_coordinates

    vertice1 = B - A
    vertice2 = C - A
    vertice3 = P - A

    dotv1 = vertice1[0]*vertice1[0] + vertice1[1]*vertice1[1]
    dotv1and2 = vertice1[0] * vertice2[0] + vertice1[1] * vertice2[1]
    dotv2 = vertice2[0]*vertice2[0] + vertice2[1] * vertice2[1]
    dotv1and3 = vertice1[0] * vertice3[0] + vertice1[1]*vertice3[1]
    dotv2and3 = vertice2[0] * vertice3[0] + vertice2[1]*vertice3[1]
    scale = dotv1 * dotv2 - dotv1and2 * dotv1and2
    v = (dotv2*dotv1and3 - dotv1 * dotv2and3) / scale
    w = (dotv1*dotv2and3 - dotv1 * dotv1and3) / scale
    u = 1 - v - w
    return np.array([u, v, w])
