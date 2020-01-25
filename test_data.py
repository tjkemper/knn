from numpy.random import randint

list3d_1 = [
    [0, 0, 0],
    [5, 0, 0],
    [-5, 0, 0],
    [5, 5, 0],
    [5, -5, 0],
    [-5, -5, 0],
    [-5, 5, 0],
    [5, 5, 5],
    [5, 5, -5],
    [5, -5, 5],
    [5, -5, -5],
    [-5, 5, 5],
    [-5, 5, -5],
    [-5, -5, 5],
    [-5, -5, -5],
]

list3d_2 = [
    [0, 0, 0],
    [5, 1, 0],
    [-5, 2, 0],
    [5, 5, 1],
    [5, -5, 2],
    [-5, -5, 3],
    [-5, 5, 4],
    [5, 5, 5],
    [5, 5, -5],
    [5, -5, 5],
    [5, -5, -5],
    [-5, 5, 5],
    [-5, 5, -5],
    [-5, -5, 5],
    [-5, -5, -5],
]

list3d_3 = [
    [0, 0, 0],
    [1, 1, 1],
    [7, 7, 7],
    [-7, -7, -7],
    [10, 10, 10],
    [-9, -9, -9],
    [-2, -2, -2],
]

list3d_4 = [
    [0, 0, 0],
    [1, 1, 1],
    [-5, -3, 3],
    [-1, 5, -5],
    [7, 7, 7],
    [-4, -4, -4],
    [2, 2, 2],
    [8, 8, 8],
    [-7, -7, -7],
    [10, 10, 10],
    [-9, -9, -9],
    [-2, -2, -2],
    [3, 3, 3],
]

list2d_1 = [
    [0, 0],
    [5, 5],
    [5, -5],
    [-5, -5],
    [-5, 5],
]

list2d_2 = [
    [0, 0],
    [5, 6],
    [5, -6],
    [-5, -5],
    [-5, 5],
]

def rand_points(num_dims, num_points=30, lo=-10, hi=10):
    l = []
    for _ in range(num_points):
        l.append(rand_point(num_dims, lo, hi))
    return l

def rand_point(num_dims, lo=-10, hi=10):
    point = []
    for _ in range(num_dims):
        point.append(randint(lo, hi))
    return point