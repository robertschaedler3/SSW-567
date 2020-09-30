# -*- coding: utf-8 -*-
"""
Updated Aug 27, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: robertschaedler3
"""

import unittest
from itertools import permutations

from hw02 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):

    def testRightTriangle(self):
        for triangle in list(permutations([3, 4, 5])):
            triangle = list(triangle)
            self.assertEqual(classifyTriangle(*triangle), 'Right',
                             f'{triangle} is a Right triangle')

    def testScaleneTriangle(self):
        for triangle in list(permutations([2, 3, 4])):
            triangle = list(triangle)
            self.assertEqual(classifyTriangle(*triangle), 'Scalene',
                             f'{triangle} is a Scalene triangle')

    def testIscoscelesTriangle(self):
        for triangle in list(permutations([2, 2, 3])):
            triangle = list(triangle)
            self.assertEqual(classifyTriangle(*triangle), 'Iscosceles',
                             f'{triangle} is an Iscoseles triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '[1, 1, 1] is an Equilaterial triangle')

    def testNotATriangle(self):
        for triangle in list(permutations([1, 1, 100])):
            triangle = list(triangle)
            self.assertEqual(classifyTriangle(*triangle),
                             'NotATriangle', f'{triangle} is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
