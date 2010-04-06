'''
Created on Sep 29, 2009

@author: changwang
'''
import unittest
import random

from edu.wmich.nodes.utils import nodes_generator


class TestUtils(unittest.TestCase):
    
    def setUp(self):
        self.rand = random.randint(1, 100)
        self.nodes = nodes_generator(self.rand)

    def testnodecount(self):
        self.assertEqual(self.rand, len(self.nodes))
        
    def testnodeid(self):
        pass
    
    def tearDown(self):
        self.rand = None
        self.nodes = None


if __name__ == "__main__":
    unittest.main()