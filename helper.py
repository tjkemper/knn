
# Visualize
def _boundaries(node, num_dims):
    boundaries = []
    for _ in range(num_dims):
      boundaries.append([None, None])
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
