__author__ = 'charles'

import unittest
from net.flyboy8869.utils.even import even


class TestEvenFunction(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even(2), "2 is an even number, so this should be 'True'")

    def test_sequence_even(self):
        l = [0, 2, 4, 6, 8, 10]
        self.assertEqual(l, [i for i in range(11) if even(i)], "Sequences don't match")

