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
        try:
            id_command = int(sys.argv[2])
        except:
            id_command = 1
    except:
        err_msg = """PLEASE SPECIFY WHAT GRAPH YOU'D LIKE TO TEST (ring(r), hypercube(hc) OR completegraph(cg)).\nYOU CAN ALSO SPECIFY THE START NODE ID (OPTIONAL).\nIF THE TEST GRAPH IS RING, THE NODE ID COULD BE FROM 1 TO 10;\nIF THE TEST GRAPH IS HYPERCUBE, THE NODE ID COULD BE FROM 1 TO 16;\nIF THE TEST GRAPH IS COMPLETEGRAPH, THE NODE ID COULD BE FROM 1 TO 12;\ne.g.: python edu/wmich/nodes/main.py ring [id] """
        sys.exit(err_msg)
    
    graph = None
    if graph_command == 'ring' or graph_command == 'r':
        if id_command < 1 or id_command > 10:
            sys.exit("THE ID SHOULD BE BETWEEN 1 AND 10")
        print "============== Ring =================="
        graph = Ring(nodes_generator(10))
        graph.connect_nodes()
        tree = tree_generator(graph, id_command)
    elif graph_command == 'hypercube' or graph_command == 'hc':
        if id_command < 1 or id_command > 16:
            sys.exit("THE ID SHOULD BE BETWEEN 1 AND 16")
        print "============== Hypercube 4 =================="
        graph = Hypercube(nodes_generator(16))
        graph.connect_nodes()
        tree = tree_generator(graph, id_command)
    elif graph_command == 'completegraph' or graph_command == 'cg':
        if id_command < 1 or id_command > 12:
            sys.exit("THE ID SHOULD BE BETWEEN 1 AND 12")
        print "============== Complete Graph =================="
        graph = CompleteGraph(nodes_generator(12))
        graph.connect_nodes()
        tree = tree_generator(graph, id_command)
    else:
        sys.exit("THE SPECIFIED GRAPH CAN'T BE HANDLED, CONTACT THE AUTHOR FOR MORE INFORMATION.")
    
    print "THE TOTAL COST IN HOPS IS: " + str(tree.branch_count())
    print
    print "THE GENERATED TREE LOOKS LIKE THIS: "
    tree.print_tree(tree.get_root())
    print
    tree.print_diameter(tree.update_weight().find_diameter(tree.get_root()))
        
