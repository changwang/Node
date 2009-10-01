'''
Created on Sep 29, 2009

@author: changwang
'''
import unittest

from edu.wmich.nodes.graph import CompleteGraph
from edu.wmich.nodes.utils import nodes_generator


class RingTestCase(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    
class CompleteGraphTestCase(unittest.TestCase):
    
    def setUp(self):
        self.cg = CompleteGraph(nodes_generator(12))
        self.cg.connect_nodes()
        
    def testChannelCount(self):
        self.assertEqual(66, self.cg.channel_count())
    
    def tearDown(self):
        self.cg = None

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RingTestCase)
    suite.addTest(CompleteGraphTestCase)
    return suite

if __name__ == "__main__":
    suite().run()