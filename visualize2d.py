import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import kdtree
import test_data
import helper

def knn(kdtree, point, result):
    _setup()
    _plot_kdtree(kdtree)
    _plot_knn(point, result)
    plt.show()

def tree(kdtree):
    _setup()
    _plot_kdtree(kdtree)
    plt.show()

def _setup():
    mpl.style.use("seaborn")
    plt.gcf().gca().axis("equal")

# KNN
def _plot_knn(point, result):
    _plot_knn_point(point)
    _plot_knn_result(result)
    _plot_knn_circle(point, result[-1][1])

def _plot_knn_point(point):
    x = point[0]
    y = point[1]
    
    plt.plot([x], [y], marker="X", markersize=20, markerfacecolor="xkcd:red")

def _plot_knn_result(point_dist_list):
    xs = [point_dist[0][0] for point_dist in point_dist_list]
    ys = [point_dist[0][1] for point_dist in point_dist_list]
    plt.scatter(xs, ys, s=100, linewidth=4, marker="x", color="xkcd:pink", alpha=1)

def _plot_knn_circle(point, radius):
    circle = plt.Circle(point, radius, alpha=0.5)
    plt.gcf().gca().add_artist(circle)

# KDTree
def _plot_kdtree(kdtree):
    _plot_points(kdtree)
    _plot_lines(kdtree)

def _plot_points(kdtree):
    xs = [point[0] for point in kdtree.point_list]
    ys = [point[1] for point in kdtree.point_list]
    plt.scatter(xs, ys, s=100, linewidth=4, marker=".", color="xkcd:red", alpha=1)

def _plot_lines(kdtree):
    _plot_lines_helper(kdtree.root, kdtree.num_dims)

def _plot_lines_helper(node, num_dims):
    if not node:
        return
    if not node.left and not node.right:
        return

    _plot_line(node, num_dims)

    _plot_lines_helper(node.left, num_dims)
    _plot_lines_helper(node.right, num_dims)

def _plot_line(node, num_dims, default_plane_width=10, num_samples=10):
    boundaries = helper._boundaries(node, num_dims)
    boundaries = boundaries[node.axis:] + boundaries[:node.axis]

    other_dim = _dim_range(boundaries[1], default_plane_width, num_samples)
    constant_dim = np.linspace(node.data[node.axis], node.data[node.axis], num_samples)

    plot_input = [constant_dim, other_dim]
    plot_input = plot_input[-node.axis:] + plot_input[:-node.axis]
    plt.plot(plot_input[0], plot_input[1], alpha=0.8)

def _dim_range(boundary, default_plane_width, num_samples):
    beg = boundary[0] if boundary[0] is not None else -default_plane_width
    end = boundary[1] if boundary[1] is not None else default_plane_width
    return np.linspace(beg, end, num_samples)

if __name__ == "__main__":

    num_dims = 2
    tree = kdtree.KDTree(test_data.list2d_1, num_dims)

    point = test_data.rand_point(num_dims)
    k = 3
    result = tree.knn(point, k)

    knn(tree, point, result)
