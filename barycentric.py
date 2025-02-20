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
def is_inside_triangle(triangle_coordinates:np.array, point_coordinates:np.array) -> bool:
    x1 = triangle_coordinates[0][0]
    x2 = triangle_coordinates[0][1]
    x3 = triangle_coordinates[0][2]
    y1 = triangle_coordinates[1][0]
    y2 = triangle_coordinates[1][1]
    y3 = triangle_coordinates[1][2]

    x, y = point_coordinates

    area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
    area1 = abs(x * (y2 - y3) + x2 * (y3 - y) + x3 * (y - y2)) / 2
    area2 = abs(x1 * (y - y3) + x * (y3 - y1) + x3 * (y1 - y)) / 2
    area3 = abs(x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)) / 2
    if area == (area1 + area2 + area3):
        return True
    else:
        return False
