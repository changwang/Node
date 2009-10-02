'''
Created on Sep 28, 2009

@author: changwang
'''

from edu.wmich.nodes.graph import Ring, CompleteGraph, Hypercube
from edu.wmich.nodes.utils import nodes_generator, tree_generator
from edu.wmich.nodes.tree import TreeKnot

if __name__ == '__main__':
    
    rg = Hypercube(nodes_generator(16))
    rg.connect_nodes()
    
    tree = tree_generator(rg, 2)
    print tree.knot_count()
    tree.print_tree()

