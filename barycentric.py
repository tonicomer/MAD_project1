%matplotlib inline
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
import numpy as np

import barycentric

def get_barycentric_coordinates(triangle_coordinates:np.ndarray, point_coordinates:np.ndarray)->np.ndarray:
    (x1,y1),(x2,y2),(x3,y3)=triangle_coordinates
    (x,y)=point_coordinates
    variables=np.array([
        [x1,x2,x3],
        [y1,y2,y3],
        [1,1,1]
        ]
    )
    results=np.array([x,y,1])
    return np.linalg.solve(variables,results)
def get_cartesian_coordinates(triangle_coordinates:np.ndarray,barycentric_coordinates:np.ndarray):
    x=triangle_coordinates[0,0]*barycentric_coordinates[0]+triangle_coordinates[0,1]*barycentric_coordinates[1]+triangle_coordinates[0,2]*barycentric_coordinates[2]
    y=triangle_coordinates[1,0]*barycentric_coordinates[0]+triangle_coordinates[1,1]*barycentric_coordinates[1]+triangle_coordinates[1,2]*barycentric_coordinates[2]
    return(x,y)
