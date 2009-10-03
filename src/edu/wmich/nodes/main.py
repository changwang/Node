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
    
    tree = tree_generator(rg, 1)
#    print tree.update_weight().find_diameter(tree.get_root())
    tree.print_tree(tree.get_root())
#    print tree.branch_count()
    
    print "============== Complete Graph =================="
    cg = CompleteGraph(nodes_generator(12))
    cg.connect_nodes()
    
    tree = tree_generator(cg, 1)
#    print tree.update_weight().find_diameter(tree.get_root())
#    print tree.branch_count()
    tree.print_tree(tree.get_root())
#    
    print "============== Hypercube 4 =================="
    hg = Hypercube(nodes_generator(16))
    hg.connect_nodes()
    
    tree = tree_generator(hg, 1)
    tree.print_tree(tree.get_root())
    
#    print tree.update_weight().find_diameter(tree.get_root())
#    print tree.branch_count()
