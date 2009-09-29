'''
Created on Sep 28, 2009

@author: changwang
'''

from edu.wmich.nodes.graph import Ring, CompleteGraph
from edu.wmich.nodes.utils import nodes_generator

if __name__ == '__main__':
    cg = CompleteGraph(nodes_generator(12))
    cg.connect_nodes()
    node1 = cg.get_node(10)
    node1.get_neighbors()
    
    rg = Ring(nodes_generator(10))
    rg.connect_nodes()
    node2 = rg.get_node(7)
    
    node2.get_neighbors()