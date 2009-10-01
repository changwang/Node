'''
Created on Sep 29, 2009

@author: changwang
'''
import unittest
import random

from edu.wmich.nodes.node import Node


class TestNode(unittest.TestCase):
    
    def setUp(self):
        self.rand = random.randint(1, 100)
        self.node = Node(self.rand)

    def testGetId(self):
        self.assertEqual(self.rand, self.node.get_id())
        
    def testGetNeighborsCount(self):
        self.assertEqual(0, self.node.get_neighbors_count())
        
    def testGetNeighborsCount2(self):
        self.assertEqual(0, len(self.node.get_neighbors()))


if __name__ == "__main__":
    unittest.main()