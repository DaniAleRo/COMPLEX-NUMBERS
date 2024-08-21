import unittest
from complex_numbers import *

class TestComplexFunctions(unittest.TestCase):
    
    def test_complex_sum(self):
        self.assertEqual(complex_sum((1, 2), (3, 4)), (4, 6))
        self.assertEqual(complex_sum((10, 9), (8, 7)), (18, 16))
    
    def test_complex_rest(self):
        self.assertEqual(complex_rest((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(complex_rest((15, 8), (15, 8)), (0, 0))

    def test_complex_multiplication(self):
        self.assertEqual(complex_multiplication((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(complex_multiplication((0, 0), (3, 4)), (0, 0))

    def test_complex_division(self):
        self.assertEqual(complex_division((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(complex_division((5, 0), (1, 0)), (5.0, 0.0))

    def test_complex_module(self):
        self.assertAlmostEqual(complex_module((3, 4)), 5)
        self.assertAlmostEqual(complex_module((0, 0)), 0)

    def test_complex_conjugated(self):
        self.assertEqual(complex_conjugated((1, 2)), (1, -2))
        self.assertEqual(complex_conjugated((-1, -2)), (-1, 2))

    def test_Cartesian_to_polar(self):
        self.assertAlmostEqual(Cartesian_to_polar((1, 1)), (math.sqrt(2), math.pi/4))
        self.assertAlmostEqual(Cartesian_to_polar((0, 0)), (0, 0))

    def test_polar_to_Cartesian(self):
        self.assertAlmostEqual(polar_to_Cartesian(math.sqrt(2), math.pi/), (1, 1))
        self.assertAlmostEqual(polar_to_Cartesian(0, 0), (0, 0))

if __name__ == '__main__':
    unittest.main()
