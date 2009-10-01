'''
Created on Sep 28, 2009

@author: changwang
'''

from edu.wmich.nodes.node import Node

class Graph:
    """ Graph represents the whole network,
    which contains the nodes in this network,
    as well as the channels.
    """

    def __init__(self, nodes):
        self.nodes = nodes

    def nodes_count(self):
        return len(self.nodes)

    def channel_count(self):
        return sum([x.get_neighbors_count() for x in self.nodes]) / 2
        

    def connect_nodes(self):
        raise NotImplementedError("You should implement this method")

    def get_node(self, id):
        for i in range(len(self.nodes)):
            if self.nodes[i].get_id() == id:
                return self.nodes[i]

class Ring(Graph):
    """ Ring graph with node connected with two nodes beside it. """
    
    def __init__(self, nodes):
        Graph.__init__(self, nodes)
        
    def connect_nodes(self):
        for i in range(len(self.nodes)):
            self.nodes[i].neighbors = self.__neighbors(self.nodes[i])
    
    def __neighbors(self, node):
        _neighbors = []
        
        if node.get_id() == 1:
            _neighbors.append(Node(len(self.nodes)))
            _neighbors.append(Node(node.get_id() + 1))
        elif node.get_id() == len(self.nodes):
            _neighbors.append(Node(1))
            _neighbors.append(Node(node.get_id() - 1))
        else:
            _neighbors.append(Node(node.get_id() - 1))
            _neighbors.append(Node(node.get_id() + 1))
        return _neighbors

class Hypercube(Graph):
    def __init__(self, nodes):
        Graph.__init__(self, nodes)
        
    def connect_nodes(self):
        pass
    
    def __neighbors(self, node):
        pass

class CompleteGraph(Graph):
    """ Complete Graph with the node connected with each other nodes """
    
    def __init__(self, nodes):
        Graph.__init__(self, nodes)

    def connect_nodes(self):
        for i in range(len(self.nodes)):
            self.nodes[i].neighbors = self.__neighbors(self.nodes[i])

    def __neighbors(self, node):
        _neighbors = []
        
        for i in range(len(self.nodes)):
            if node.get_id() != self.nodes[i].get_id():
                _neighbors.append(self.nodes[i])
        return _neighbors
