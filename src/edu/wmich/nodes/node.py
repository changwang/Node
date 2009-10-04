#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Sep 28, 2009
@author: changwang
'''

class Node:
    """ Node represents the node in the network,
        which contains its identification
        and its neighbor's identification.
        Between two nodes, there is a bidirectional channel. """

    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def get_id(self):
        return self.id
    
    def has_neighbors(self):
        return len(self.neighbors) > 0

    def get_neighbors(self):
        return self.neighbors
    
    def set_neighbors(self, neighbors=[]):
        self.neighbors = neighbors

    def get_neighbors_count(self):
        return len(self.neighbors)

    def __repr__(self):
        return "Node: " + str(self.id)
