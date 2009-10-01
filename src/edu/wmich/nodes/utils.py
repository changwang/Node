'''
Created on Sep 28, 2009

@author: changwang
'''
from edu.wmich.nodes.node import *
from edu.wmich.nodes.tree import *

def nodes_generator(count):
    nodes = []
    for i in range(1, count+1):
        nodes.append(Node(i))
    return nodes

def tree_generator(graph, root_id):
    root = TreeKnot(graph.get_node(root_id))
    root.init_children()
                
    tree = Tree(root)
    
    temp_children = root.get_children()
    for knot in temp_children:
        if tree.has_knot(knot):
            continue
        else:
            knot.init_children()
            tree.add_knot(knot)
            for k in knot.get_children():
#                k = TreeKnot(i)
                if tree.has_knot(k):
                    pass
                else:
                    temp_children.extend(knot.get_children())
            temp_children.remove(knot)
#    
#    temp_children = root.get_children()
#    for n in temp_children:
#        if n in tree:
#            continue
#        else:
#            tree.add_node(parent, child)
#            temp_children.append(n.get_neighbors())
    
#    if len(root.children) > 0:
#        for child in root.children:
#            tree.add_node(root, child)
    
    return tree

#def tree_generator(graph, root_node):
#    tree = {}
#    __insert_node(tree, root_node)
#    if (root_node.has_neighbors()):
#        for i in root_node.get_neighbors():
#            __insert_node(tree, graph.get_node(i))
#            
#    return tree
#
#def __insert_node(tree, node):
#    if (node.get_id() in tree):
#        pass
#    else:
#        tree[node.get_id()] = tuple(node.get_neighbors())
#    
#    return tree
