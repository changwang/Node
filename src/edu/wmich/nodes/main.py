'''
Created on Sep 28, 2009

@author: changwang
'''

from edu.wmich.nodes.graph import Ring, CompleteGraph
from edu.wmich.nodes.utils import nodes_generator, tree_generator
from edu.wmich.nodes.tree import TreeKnot

if __name__ == '__main__':
    
    rg = Ring(nodes_generator(10))
    rg.connect_nodes()
#    print rg
    print tree_generator(rg, 2).knot_count()
#    TreeKnot(rg.get_node(2))