import sys


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


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python .\hw01.py <length A> <length B> <length C>')
    else:
        try:
            sides = list(map(int, sys.argv[1:]))
            assert (all(side > 0 for side in sides))
            result = classify_triangle(*sides)
            print(f'{"Not a" if result == "NotATriangle" else result} triangle')
        except:
            print('Invalid side length given. Sides must be positive integers.')
