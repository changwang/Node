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
                
    tree = Tree(root)
    root.init_children(tree)
    
    temp_children = root.get_children()[:]
    while(temp_children):
        knot = temp_children[0]
        if tree.has_knot(knot):
            temp_children.remove(knot)
        else:
            __init_children(knot, temp_children)
            tree.add_knot(knot)
            for k in knot.get_children():
                if tree.has_knot(k) or __in_temp(k, temp_children):
                    pass
                else:
                    temp_children.append(k)
            temp_children.remove(knot)
    
    return tree

def __init_children(knot, tmp_list):
    if not tmp_list:
        return
    for n in knot.data.get_neighbors():
        if __in_temp(TreeKnot(n), tmp_list):
            continue
        else:
            knot.get_children().append(TreeKnot(n))

def __in_temp(tk, tmp_list):
    flag = False
    for t in tmp_list:
        if tk.get_data().get_id() == t.get_data().get_id():
            flag = True
            
    return flag