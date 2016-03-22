'''
Unit test for SayHiClass son src


@author: luzC
'''
import unittest
from  demo.src.say_hi import SayHiClass


class SayHiTestCase(unittest.TestCase):

    def setUp(self):
        print "Unit test case setup"
        super(SayHiTestCase, self).setUp()
        self.say = SayHiClass()

    def test_hi(self):
        self.say.hi()
        self.say.hi('Luz')

    def test_f_sum(self):
        self.say.a_sum([1,2,3,4])

if __name__ == '__main__':
    unittest.main()

