
import enum
import math
import test_data
import visualize3d

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

class VisualType(enum.Enum):
    textual=1
    graphical=2

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
        median = len(point_sorted_list) // 2
        median_value = point_sorted_list[median][axis]

        # Ensure points with same axis value are moved to the right side of the tree.
        # This violates the halveness property, but allows simple (efficient?) knn search.
        split_index = median
        while split_index >= 1 and point_sorted_list[split_index - 1][axis] == median_value:
            split_index -= 1
        split_point = point_sorted_list[split_index]

        node = Node()
        node.data = split_point
        node.left = self._build(point_sorted_list[:split_index], depth + 1, node)
        node.right = self._build(point_sorted_list[split_index + 1:], depth + 1, node)
        node.parent = parent
        node.axis = axis
        node.depth = depth
        return node

    def knn(self, point, k):
        # k_best = [[point, dist], [point, dist], ...]
        k_best = []
        self._knn_helper(self.root, point, k, k_best)
        return k_best

    def _knn_helper(self, curr_node, point, k, k_best):
        if not curr_node:
            return

        # Recurse
        recurse_right = True
        if point[curr_node.axis] >= curr_node.data[curr_node.axis]:
            self._knn_helper(curr_node.right, point, k, k_best)
        elif point[curr_node.axis] < curr_node.data[curr_node.axis]:
            recurse_right = False
            self._knn_helper(curr_node.left, point, k, k_best)
        else:
            print("knn: Should never reach this point.")

        curr_dist = kd_dist(curr_node.data, point)
        if len(k_best) < k or curr_dist < k_best[-1][1]:
            self._knn_insort(k_best, [curr_node.data, curr_dist])
        
        if len(k_best) > k:
            k_best.pop()

        # Check if distance to splitting plane is less than the worst k_best distance.
        # If so, there could be closer neighbors in that subtree.
        worst_k_best_dist = k_best[-1][1]
        dist_to_splitting_plane = abs(curr_node.data[curr_node.axis] - point[curr_node.axis])

        if len(k_best) < k or dist_to_splitting_plane < worst_k_best_dist:
            node_to_check = curr_node.left if recurse_right else curr_node.right
            self._knn_helper(node_to_check, point, k, k_best)
        
    def _knn_insort(self, point_dist_list, point_dist):
        lo, hi = 0, len(point_dist_list)

        while lo < hi:
            mid = (lo + hi) // 2
            if point_dist[1] >= point_dist_list[mid][1]:
                lo = mid + 1
            else:
                hi = mid
        point_dist_list.insert(lo, point_dist)

    # Todo: implement w/ balance invariant
    # https://en.wikipedia.org/wiki/K-d_tree#Balancing
    def add(self, point):
        pass
    def remove(self, point):
        pass

    def visualize(self, visual_type=VisualType.textual):
        if visual_type == VisualType.textual:
            print(self.root)
        elif visual_type == VisualType.graphical:
            if self.num_dims < 1 or self.num_dims > 3:
                raise ValueError("Dimensions must be 1, 2, or 3.")
            
            if self.num_dims == 1:
                raise NotImplementedError("Insert 25 cents")
            elif self.num_dims == 2:
                raise NotImplementedError("Insert 25 cents")
            elif self.num_dims == 3:
                visualize3d.tree(self)

        else:
            raise ValueError("Invalid VisualType.")
    
    # TODO: Implement VisualType.textual
    def visualize_knn(self, point, result, visual_type=VisualType.graphical):
        if visual_type != VisualType.graphical:
            raise ValueError("Only VisualType.graphical is supported.")

        if self.num_dims < 1 or self.num_dims > 3:
            raise ValueError("Dimensions must be 1, 2, or 3.")

        if self.num_dims == 1:
            raise NotImplementedError("Insert 25 cents")
        elif self.num_dims == 2:
            raise NotImplementedError("Insert 25 cents")
        elif self.num_dims == 3:
            visualize3d.knn(self, point, result)

def kd_dist(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have same number of dimensions.")
    
    result = 0
    for i in range(len(point1)):
        result += (point1[i] - point2[i]) ** 2

    result = math.sqrt(result)
    return result

if __name__ == "__main__":
    tree = KDTree(test_data.list2, 3)

    point = [5, 5, 4]
    k = 7
    result = tree.knn(point, k)

    tree.visualize(visual_type=VisualType.graphical)
    # tree.visualize_knn(point, result)
