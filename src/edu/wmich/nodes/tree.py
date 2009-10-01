'''
Created on Oct 1, 2009

@author: changwang
'''

class TreeKnot:
    def __init__(self, node):
        self.data = node
        self.weight = 1
#        self.parent = None
        self.children = []
#        for n in node.get_neighbors():
#            self.children.append(TreeKnot(n))
    
    def add_child(self, child):
        self.children.append(child)
        
#    def add_parent(self, parent):
#        self.parent = parent

    def init_children(self):
        for n in self.data.get_neighbors():
            self.children.append(TreeKnot(n))
        
    def get_children(self):
        return self.children
        
    def __str__(self):
        return str(self.data.get_id())
    
        
    
class Tree:
    
    def __init__(self, root_knot):
        self.tree = {}
        self.root_knot = root_knot
        self.tree[root_knot.data.get_id()] = root_knot
        
    def add_knot(self, knot):
        self.tree[knot.data.get_id()] = knot
        
    def has_knot(self, knot):
        if knot.data.get_id() in self.tree:
            return True
        else:
            return False
        
    def knot_count(self):
        return len(self.tree.items())
