#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 28, 2009
@author: changwang
'''

class Graph:
    """ Graph represents the whole network,
    which contains the nodes in this network,
    as well as the channels. """

    def __init__(self, nodes):
        self.nodes = nodes
        
    def get_nodes(self):
        """ return the total nodes in this graph. """
        return self.nodes

    def nodes_count(self):
        """ return the total nodes count in this graph. """
        return len(self.nodes)

    def channel_count(self):
        """ return the total channels in this graph. """
        return sum([x.get_neighbors_count() for x in self.get_nodes()]) / 2

    def connect_nodes(self):
        """ This method is a virtual method,
            each subclass should implement this method,
            because each subclass has its own connections between nodes. """
        raise NotImplementedError("You should implement this method")

    def get_node(self, id):
        """ return the node specified by the id. """
        for node in self.get_nodes():
            if node.get_id() == id:
                return node
        # if the specified node is not exist in this graph.
        return None

class Ring(Graph):
    """ Ring graph with node connected with two nodes beside it. """
    def __init__(self, nodes):
        Graph.__init__(self, nodes)
        
    def connect_nodes(self):
        for node in self.get_nodes():
            node.set_neighbors(self.__neighbors(node))
    
    def __neighbors(self, node):
        _neighbors = []
        
        if node.get_id() == 1:
            _neighbors.append(self.get_node(node.get_id() + 1))
            _neighbors.append(self.get_node(self.nodes_count()))
        elif node.get_id() == self.nodes_count():
            _neighbors.append(self.get_node(node.get_id() - 1))
            _neighbors.append(self.get_node(1))
        else:
            _neighbors.append(self.get_node(node.get_id() - 1))
            _neighbors.append(self.get_node(node.get_id() + 1))
        return _neighbors

class Hypercube(Graph):
    """ Hypercube 4 with node connected with four nodes beside it. """
    def __init__(self, nodes):
        Graph.__init__(self, nodes)
        
    def connect_nodes(self):
        for node in self.get_nodes():
            node.set_neighbors(self.__neighbors(node))
    
    def __neighbors(self, node):
        _neighbors = []
        id = node.get_id()
        
        if id % 4 == 1:
            _neighbors.append(self.get_node(id+1))
            _neighbors.append(self.get_node(id+3))
        elif id % 4 == 2 or id % 4 == 3:
            _neighbors.append(self.get_node(id-1))
            _neighbors.append(self.get_node(id+1))
        elif id % 4 == 0:
            _neighbors.append(self.get_node(id-3))
            _neighbors.append(self.get_node(id-1))
            
        if id <= 8:
            if id <= 4:
                _neighbors.append(self.get_node(id+4))
            else:
                _neighbors.append(self.get_node(id-4))
            _neighbors.append(self.get_node(id+8))
        else:
            _neighbors.append(self.get_node(id-8))
            if id <=8:
                _neighbors.append(self.get_node(id+4))
            else:
                _neighbors.append(self.get_node(id-4))
        return _neighbors

class CompleteGraph(Graph):
    """ Complete Graph with the node connected with each other nodes. """
    def __init__(self, nodes):
        Graph.__init__(self, nodes)

    def connect_nodes(self):
        for node in self.get_nodes():
            node.set_neighbors(self.__neighbors(node))

    def __neighbors(self, node):
        _neighbors = []
        
        for n in self.get_nodes():
            if n.get_id() != node.get_id():
                _neighbors.append(n)
        return _neighbors
