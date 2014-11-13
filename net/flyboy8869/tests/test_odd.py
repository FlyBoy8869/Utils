__author__ = 'charles'

import unittest
from net.flyboy8869.utils.odd import odd


class TestEvenFunction(unittest.TestCase):

    def test_odd(self):
        self.assertTrue(odd(3), "3 is an odd number, so this should be 'True'")
