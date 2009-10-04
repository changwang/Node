#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Oct 1, 2009
@author: changwang
'''

class TreeKnot:
    """ TreeKnot represents the knot in a tree. """
    
    def __init__(self, node):
        self.data = node
        self.weight = 1
        self.children = []
    
    def add_child(self, child):
        """ add a new child to current treeknot """
        self.children.append(child)
        
    def get_data(self):
        return self.data

    def init_children(self, tree):
        """ Add necessary knot to current children list,
            if the child is not the treeknot in the tree, add it. """
        for n in self.get_data().get_neighbors():
            if not tree.has_knot(TreeKnot(n)):
                self.children.append(TreeKnot(n))
        
    def get_children(self):
        return self.children
    
    def get_children_count(self):
        return len(self.children)
    
    def get_weight(self):
        return self.weight
            
    def update_weight(self):
        """ update the weight of the treeknot, recursively. """
        if self.get_children_count() == 0:
            self.weight = 1
        else:
            self.weight += sum([x.update_weight() for x in self.get_children()])            
        return self.weight
    
    def is_leaf(self):
        """ whether this knot is a leaf in the tree. """
        return self.get_children_count() == 0
    
    def __repr__(self):
        return "TreeKnot: " + str(self.data.get_id())
        
class Tree:
    """ This tree is used to find the efficient way of broadcasting the msg from one
    node to the other nodes and the diameter of the graph. """
    
    def __init__(self, root_knot):
        self.tree = {}
        self.root_knot = root_knot
        self.tree[root_knot.get_data().get_id()] = root_knot
        self.path = [self.root_knot]
        
    def add_knot(self, knot):
        indexes = []
        """ this step is used to remove the knot(s) which is existed in the tree
         from the children list of current knot. """
        for n in knot.get_children():
            if self.has_knot(n):
                indexes.append(n)
        
        for n in indexes:
            knot.get_children().remove(n)
        
        self.tree[knot.data.get_id()] = knot
        
    def get_root(self):
        """ return the root knot of this tree. """
        return self.root_knot
    
    def get_knot(self, id):
        """ return the knot specified by the id in current tree. """
        if id not in self.tree:
            return None
        return self.tree.get(id)
        
    def has_knot(self, knot):
        """ find out whether one knot is in the tree. """
        if knot.get_data().get_id() in self.tree:
            return True
        else:
            return False

    def knot_count(self):
        return len(self.tree)
    
    def get_knot_parent(self, knot):
        """ find out the parent knot of current knot in the tree. """
        for key, value in self.tree.items():
            if knot in value.get_children():
                return self.get_knot(key)
        return None
    
    def print_tree(self, node):
        """ print out the tree with a user-friendly way. """
        if node.is_leaf():
            print '----- ↑ -----'
            print '----- ♧ ----'
            print '✂ -----------'
            return
        for n in node.get_children():
            print '-------------'
            print self.get_knot_parent(n).get_data()
            print '----- ↓ -----'
            print n.get_data()
            self.print_tree(n)

    def leaves(self):
        """ return all the leaves in the tree. """
        leaves = []
        for knot in self.tree.values():
            if knot.get_children_count() == 0:
                leaves.append(knot)
        return leaves
        
    def update_weight(self):
        """ update the nodes' weight in the tree.
            so we can find the diameter of the graph with it. """
        self.root_knot.update_weight()
        return self
    
    def branch_count(self):
        """ get the total hops in the tree. """
        sum = 0
        for n in self.tree.values():
            sum += n.get_children_count()
        return sum
    
    def __find_max_children(self, knot):
        """ find the max weight treeknot from the children list. """
        if knot.get_children_count() == 0:
            return knot
        else:
            max = knot.get_children()[0]
            for child in knot.get_children():
                if max.get_weight() < child.get_weight():
                    max = child
                    
            return max
    
    def find_diameter(self, node):
        """ find the diameter of the graph using the weight of each treeknot. """
        if node.is_leaf():
            return None
        else:
            m = self.__find_max_children(node)
            self.path.append(m)
            self.find_diameter(m)
        return self.path
    
    def print_diameter(self, path):
        print 'THE LENGTH OF THE DIAMETER IS: ' + str(len(path))
        print 'AND THE PATH IS: '
        for n in path:
            if n == path[-1]:
                print str(n.get_data())
            else:
                print str(n.get_data()) + ' ➡ ',
