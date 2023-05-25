import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 10, "test"), "test")
        self.assertEqual(arrs.get([1, 4, 2, 7, 9], 2), 2)
        self.assertEqual(arrs.get([1, 2, 3], 3, "test"), "test")
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, -1), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, 0), [])
        self.assertEqual(arrs.my_slice([], 0, 0), [])
        self.assertEqual(arrs.my_slice([1], -2, 0), [])
        self.assertEqual(arrs.my_slice([1], -1, 0), [])
