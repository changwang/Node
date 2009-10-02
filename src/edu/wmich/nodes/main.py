'''
Created on Sep 28, 2009

@author: changwang
'''

from edu.wmich.nodes.graph import Ring, CompleteGraph, Hypercube
from edu.wmich.nodes.utils import nodes_generator, tree_generator

if __name__ == '__main__':
    
    print "============== Ring =================="
    rg = Ring(nodes_generator(10))
    rg.connect_nodes()
    
    tree = tree_generator(rg, 2)
    print tree.leaves()
    
    print tree.update_weight().find_diameter(tree.get_root())
    
    print "============== Complete Graph =================="
    cg = CompleteGraph(nodes_generator(12))
    cg.connect_nodes()
    
    tree = tree_generator(cg, 2)
    print tree.leaves()
    
    print tree.update_weight().find_diameter(tree.get_root())
    
    print 
    
    print "============== Hypercube 4 =================="
    hg = Hypercube(nodes_generator(16))
    hg.connect_nodes()
    
    tree = tree_generator(hg, 2)
    print tree.leaves()
    
    print tree.update_weight().find_diameter(tree.get_root())
    
    print 