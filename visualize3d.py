import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import kdtree
import test_data

def knn(kdtree, point, result):
    ax = _setup()
    _plot_kdtree(ax, kdtree)
    _plot_knn(ax, point, result)
    plt.show()

def tree(kdtree):
    ax = _setup()
    _plot_kdtree(ax, kdtree)
    plt.show()

def _setup():
    mpl.style.use("seaborn")
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    return ax

# KNN
def _plot_knn(ax, point, result):
    _plot_knn_point(ax, point)
    _plot_knn_result(ax, result)
    _plot_knn_sphere(ax, point, result[-1][1])

def _plot_knn_point(ax, point):
    x = point[0]
    y = point[1]
    z = point[2]
    ax.plot([x], [y], [z], marker="X", markersize=20, markerfacecolor="xkcd:red")

def _plot_knn_result(ax, point_dist_list):
    xs = [point_dist[0][0] for point_dist in point_dist_list]
    ys = [point_dist[0][1] for point_dist in point_dist_list]
    zs = [point_dist[0][2] for point_dist in point_dist_list]
    ax.scatter(xs, ys, zs, s=100, linewidth=4, marker="x", color="xkcd:pink", alpha=1)

def _plot_knn_sphere(ax, point, radius):
    u = np.linspace(0, 2* np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v)) + point[0]
    y = radius * np.outer(np.sin(u), np.sin(v)) + point[1]
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + point[2]
    ax.plot_surface(x, y, z, color='b', rstride=4, cstride=4, alpha=0.2)

# KDTree
def _plot_kdtree(ax, kdtree):
    _plot_points(ax, kdtree)
    _plot_planes(ax, kdtree)

def _plot_points(ax, kdtree):
    xs = [point[0] for point in kdtree.point_list]
    ys = [point[1] for point in kdtree.point_list]
    zs = [point[2] for point in kdtree.point_list]
    ax.scatter(xs, ys, zs, s=100, linewidth=4, marker=".", color="xkcd:yellow", alpha=1)

def _plot_planes(ax, kdtree):
    _plot_planes_helper(ax, kdtree.root, kdtree.num_dims)

def _plot_planes_helper(ax, node, num_dims):
    if not node:
        return
    if not node.left and not node.right:
        return

    _plot_plane(ax, node, num_dims)

    _plot_planes_helper(ax, node.left, num_dims)
    _plot_planes_helper(ax, node.right, num_dims)

def _plot_plane(ax, node, num_dims, default_plane_width=10, num_samples=10):
    boundaries = _boundaries(node)
    boundaries = boundaries[node.axis:] + boundaries[:node.axis]
    
    child_dim = _dim_range(boundaries[1], default_plane_width, num_samples)
    grandchild_dim = _dim_range(boundaries[2], default_plane_width, num_samples)
    child_matrix, grandchild_matrix  = np.meshgrid(child_dim, grandchild_dim)

    constant_dim = np.linspace(node.data[node.axis], node.data[node.axis], num_samples)
    constant_matrix, _ = np.meshgrid(constant_dim, constant_dim)

    plot_input = [constant_matrix, child_matrix, grandchild_matrix]
    plot_input = plot_input[-node.axis:] + plot_input[:-node.axis]
    ax.plot_surface(plot_input[0], plot_input[1], plot_input[2], alpha=0.8)

def _dim_range(boundary, default_plane_width, num_samples):
    beg = boundary[0] if boundary[0] is not None else -default_plane_width
    end = boundary[1] if boundary[1] is not None else default_plane_width
    return np.linspace(beg, end, num_samples)

def _boundaries(node):
    boundaries = [[None, None], [None, None], [None, None]]
    _boundaries_helper(node, node.parent, boundaries)
    return boundaries

def _boundaries_helper(node, ancestor, boundaries):
    if not ancestor:
        return
    
    if node.axis != ancestor.axis:
        if node.data[ancestor.axis] >= ancestor.data[ancestor.axis]:
            if boundaries[ancestor.axis][0] is None or ancestor.data[ancestor.axis] > boundaries[ancestor.axis][0]:
                boundaries[ancestor.axis][0] = ancestor.data[ancestor.axis]
        else:
            if boundaries[ancestor.axis][1] is None or ancestor.data[ancestor.axis] < boundaries[ancestor.axis][1]:
                boundaries[ancestor.axis][1] = ancestor.data[ancestor.axis]

    _boundaries_helper(node, ancestor.parent, boundaries)

if __name__ == "__main__":

    tree = kdtree.KDTree(test_data.list4, 3)

    point = [5, 5, 4]
    k = 7
    result = tree.knn(point, k)

    knn(tree, point, result)
