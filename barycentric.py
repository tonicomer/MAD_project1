import numpy as np
def get_barycentric_coordinates(triangle_coordinates:np.ndarray, point_coordinates:np.ndarray)->np.ndarray:
    (x1,y1),(x2,y2),(x3,y3)=triangle_coordinates   ## Extracting the (x,y) coordinates of the 3 vertices in the triangle
    (x,y)=point_coordinates  ## Extracting the (x,y) coordinates of the input point
    variables=np.array([   ## Constructs a 3x3 array (matrix) that consists of the triangle points
        [x1,x2,x3],
        [y1,y2,y3],
        [1,1,1]  ## All ones so that the coordinates add up to 1
        ]
    )
    results=np.array([x,y,1])  ## represents the coordinates we are trying to calculate
    return np.linalg.solve(variables,results) ## Using this function from a previous homework assignment to solve the unknown lambda values

## The function above is calculating barycentric coordinates for a given point.
def get_cartesian_coordinates(triangle_coordinates:np.ndarray,barycentric_coordinates:np.ndarray):
    x=triangle_coordinates[0,0]*barycentric_coordinates[0]+triangle_coordinates[0,1]*barycentric_coordinates[1]+triangle_coordinates[0,2]*barycentric_coordinates[2]
    y=triangle_coordinates[1,0]*barycentric_coordinates[0]+triangle_coordinates[1,1]*barycentric_coordinates[1]+triangle_coordinates[1,2]*barycentric_coordinates[2]
    return(x,y)

## The function get_cartesian_coordinates() is taking barycentric coordinates and converting them back to cartesian coordinates. 
## It is reversing the previous function. It uses the given formula to solve. 
def is_inside_triangle(triangle_coordinates:np.array, point_coordinates:np.array) -> bool:
    x1 = triangle_coordinates[0][0]
    x2 = triangle_coordinates[0][1]
    x3 = triangle_coordinates[0][2]    ## These lines are extracting each coordinate from the input triangle_coordinates
    y1 = triangle_coordinates[1][0]
    y2 = triangle_coordinates[1][1]
    y3 = triangle_coordinates[1][2]

    x, y = point_coordinates    ## Also extracting (x,y) points

    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2    ## This line finds the area of the triangle overall
    area1 = abs(x * (y2 - y3) + x2 * (y3 - y) + x3 * (y - y2)) / 2    ## Areas 1,2, and 3 are finding the sub triangles
    area2 = abs(x1 * (y - y3) + x * (y3 - y1) + x3 * (y1 - y)) / 2    ## One vertex is replaced with a test point in each sub triangle
    area3 = abs(x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)) / 2
    if area == (area1 + area2 + area3):        ## Checks if the total triangle area is equal to the sum of each sub triangle
        return True    ## The point is inside or on the boundary if the if statement is true, otherwise we return False
    else:
        return False
