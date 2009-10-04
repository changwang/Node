#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 28, 2009
@author: changwang
'''
from edu.wmich.nodes.node import Node
from edu.wmich.nodes.tree import TreeKnot, Tree

def nodes_generator(count):
    """ generate a serial of nodes counted on the total number. """

    nodes = []
    for i in range(1, count+1):
        nodes.append(Node(i))
    return nodes

def tree_generator(graph, root_id):
    """ generate the final tree which represents 
        the path of broadcasting a message from one node to others. """

    root = TreeKnot(graph.get_node(root_id))
    tree = Tree(root)
    root.init_children(tree)

    # get a copy of root's children list,
    # otherwise modifying temp_children will still change root's children list.
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
    """ add children to specified knot. """

    if not tmp_list:
        return
    for n in knot.get_data().get_neighbors():
        if __in_temp(TreeKnot(n), tmp_list):
            continue
        else:
            knot.get_children().append(TreeKnot(n))

def __in_temp(tk, tmp_list):
    """ whether the specified knot is in the temporary list. """

    flag = False
    for t in tmp_list:
        if tk.get_data().get_id() == t.get_data().get_id():
            flag = True
    return flag