'''
Created on Oct 1, 2009

@author: changwang
'''

class TreeKnot:
    def __init__(self, node):
        self.data = node
        self.weight = 1
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        
    def get_data(self):
        return self.data

    def init_children(self, tree):
        for n in self.data.get_neighbors():
            if not tree.has_knot(TreeKnot(n)):
                self.children.append(TreeKnot(n))
        
    def get_children(self):
        return self.children
    
    def get_children_count(self):
        return len(self.children)
    
    def get_weight(self):
        return self.weight
            
    def update_weight(self):
        if self.get_children_count() == 0:
            self.weight = 1
        else:
            self.weight += sum([x.update_weight() for x in self.get_children()])
            
        return self.weight
    
    def is_leaf(self):
        return self.get_children_count() == 0
    
    def __repr__(self):
        return "TreeKnot: " + str(self.data.get_id())
        
class Tree:
    
    def __init__(self, root_knot):
        self.tree = {}
        self.root_knot = root_knot
        self.tree[root_knot.data.get_id()] = root_knot
        
    def add_knot(self, knot):
        indexes = []
        for i in range(len(knot.get_children())):
            if self.has_knot(knot.get_children()[i]):
                indexes.append(knot.get_children()[i])
        
        for n in indexes:
            knot.get_children().remove(n)
        
        self.tree[knot.data.get_id()] = knot
        
    def get_root(self):
        return self.root_knot
        
    def has_knot(self, knot):
        if knot.data.get_id() in self.tree:
            return True
        else:
            return False
        
    def knot_count(self):
        return len(self.tree.items())
    
    def print_tree(self):
        pass
    
    def leaves(self):
        leaves = []
        for knot in self.tree.values():
            if knot.get_children_count() == 0:
                leaves.append(knot)
        return leaves
    
    def root_weight(self):
        return self.__weight(self.root_knot)
    
    def update_weight(self):
        self.root_knot.update_weight()
        return self
    
    def __find_max_children(self, knot):
        if knot.get_children_count() == 0:
            return knot
        else:
            max = knot.get_children()[0]
            for x in knot.get_children():
                if max.get_weight() < x.get_weight():
                    max = x
                    
            return max
    
    def find_diameter(self, node):
        path = []
        if node.is_leaf():
            path.append(node)
            return path
        else:
            m = self.__find_max_children(node)
            psub = self.find_diameter(m)[:]
            path.extend(psub)
#            path.extend(self.find_diameter(self.__find_max_children(node)))
        return path
        
