__author__ = 'charles'

import unittest
from net.flyboy8869.utils.odd import odd


class TestEvenFunction(unittest.TestCase):

    def test_odd(self):
        self.assertTrue(odd(3), "3 is an odd number, so this should be 'True'")

    def test_sequence_odd(self):
        l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
        self.assertEqual(l, [i for i in range(22) if odd(i)], "Sequences are not equal")
