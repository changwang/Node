'''
Created on Sep 28, 2009

@author: changwang
'''

class Node:
    """ Node represents the node in the network,
        which contains its identification
        and its neighbor's identification.
        Between two nodes, there is a bidirectional channel.
        """
    
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def broadcast(self, msg):
        pass

    def __str__(self):
        return str(self.id)

    def get_id(self):
        return self.id

    def get_neighbors(self):
        for i in range(len(self.neighbors)):
            print self.neighbors[i]

    def get_neighbors_count(self):
        return len(self.neighbors)

