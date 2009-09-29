'''
Created on Sep 28, 2009

@author: changwang
'''

from edu.wmich.nodes.graph import CompleteGraph
from edu.wmich.nodes.utils import nodes_generator

if __name__ == '__main__':
    cg = CompleteGraph(nodes_generator(12))
    cg.connect_nodes()
    node = cg.get_node(1)
    
    node.get_neighbors(),