__author__ = 'charles'

import unittest
from net.flyboy8869.utils.even import even


class TestEvenFunction(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even(2), "2 is an even number, so this should be 'True'")
