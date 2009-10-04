#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 28, 2009
@author: changwang
'''

import sys
from edu.wmich.nodes.graph import Ring, CompleteGraph, Hypercube
from edu.wmich.nodes.utils import nodes_generator, tree_generator

if __name__ == '__main__':
    try:
        graph_command = sys.argv[1]
    except:
        print "PLEASE SPECIFY WHAT GRAPH YOU'D LIKE TO TEST (ring(r), hypercube(hc) OR completegraph(cg))."
        print "e.g.: python edu/wmich/nodes/main.py ring"
        exit()
    
    graph = None
    if graph_command == 'ring' or graph_command == 'r':
        print "============== Ring =================="
        graph = Ring(nodes_generator(10))
        graph.connect_nodes()
        tree = tree_generator(graph, 1)
    elif graph_command == 'hypercube' or graph_command == 'hc':
        print "============== Hypercube 4 =================="
        graph = Hypercube(nodes_generator(16))
        graph.connect_nodes()
        tree = tree_generator(graph, 1)
    elif graph_command == 'completegraph' or graph_command == 'cg':
        print "============== Complete Graph =================="
        graph = CompleteGraph(nodes_generator(12))
        graph.connect_nodes()
        tree = tree_generator(graph, 1)
    else:
        print "THE SPECIFIED GRAPH CAN'T BE HANDLED, CONTACT THE AUTHOR FOR MORE INFORMATION."
        exit()
    print "THE TOTAL COST IN HOPS IS: " + str(tree.branch_count())
    print
    print "THE GENERATED TREE LOOKS LIKE THIS: "
    tree.print_tree(tree.get_root())
    print
    tree.print_diameter(tree.update_weight().find_diameter(tree.get_root()))
        
