"""
This file shows some simple python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

@author: robertschaedler3
"""

import sys
import unittest


def classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        elif a ** 2 + b ** 2 == c ** 2:
            return 'Right'
        else:
            return 'Scalene'
    else:
        return 'NotATriangle'


class TestTriangles(unittest.TestCase):

    def testEquilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 is an equilateral triangle')

    def testIsosceles(self):
        self.assertEqual(classify_triangle(1, 2, 2),
                         'Isosceles', '1,2,2 is an isosceles triangle')
        self.assertEqual(classify_triangle(2, 1, 2),
                         'Isosceles', '2,1,2 is an isosceles triangle')
        self.assertEqual(classify_triangle(2, 2, 1),
                         'Isosceles', '2,2,1 is an isosceles triangle')

    def testRight(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def testScalene(self):
        self.assertEqual(classify_triangle(5, 7, 9), 'Scalene',
                         '5,7,9 is a Right triangle')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(1, 1, 100), 'NotATriangle',
                         '1,1,100 is not a triangle')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main(exit=False)
    elif len(sys.argv) != 4:
        print('Usage: python .\hw01.py <length A> <length B> <length C>')
    else:
        try:
            sides = list(map(int, sys.argv[1:]))
            assert (all(side > 0 for side in sides))
            result = classify_triangle(*sides)
            print(f'{"Not a" if result == "NotATriangle" else result} triangle')
        except:
            print('Invalid side length given. Sides must be positive integers.')
