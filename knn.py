import math

def knn(point_list, point, k=1):
    dist_list = []
    for p in point_list:
        dist_list.append([p, dist(p, point)])

    dist_sorted_list = sorted(dist_list, key=lambda obj: obj[1])
    return dist_sorted_list[:k]

def dist(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    return math.sqrt(a ** 2 + b ** 2)

if __name__ == "__main__":
    list1 = [[0, 0], [0, 1], [0, 2], [1, 1], [-1, 0], [-1, -1]]
    point1 = [0, 0]
    print(point1, knn(list1, point1, k=4))
