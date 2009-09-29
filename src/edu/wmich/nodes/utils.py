'''
Created on Sep 28, 2009

@author: changwang
'''
from edu.wmich.nodes.node import *

def nodes_generator(count):
    nodes = []
    for i in range(1, count+1):
        nodes.append(Node(i))
    return nodes
