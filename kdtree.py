
class Node:
    def __init__(self, data=None, left=None, right=None, parent=None, axis=None, depth=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.axis = axis
        self.depth = depth
    
    def __str__(self, level=0):
        string = "\t" * level + str(self.data) + "\n"
        if self.left:
            string += self.left.__str__(level + 1)
        else:
            string += "\t" * (level + 1) + "None" + "\n"
        if self.right:
            string += self.right.__str__(level + 1)
        else:
            string += "\t" * (level + 1) + "None" + "\n"
        return string

# https://en.wikipedia.org/wiki/K-d_tree
class KDTree:

    def __init__(self, point_list, num_dims):
        self.point_list = point_list
        self.num_dims = num_dims
        self.root = self._build(self.point_list, 0, None)

    def _build(self, point_list, depth, parent):
        if not point_list:
            return None

        axis = depth % self.num_dims

        point_sorted_list = sorted(point_list, key=lambda point: point[axis])
        mid = int(len(point_sorted_list) / 2)

        node = Node()
        node.data = point_sorted_list[mid]
        node.left = self._build(point_sorted_list[:mid], depth + 1, node)
        node.right = self._build(point_sorted_list[mid+1:], depth + 1, node)
        node.parent = parent
        node.axis = axis
        node.depth = depth
        return node

    # Todo: implement
    def knn(self, k): 
        pass

    # Todo: implement w/ balance invariant
    def add(self, point):
        pass
    def remove(self, point):
        pass

if __name__ == "__main__":
    kdtree = KDTree([
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
        ],
        3)

    print(kdtree.root)
