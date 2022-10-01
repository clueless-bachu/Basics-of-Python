import unittest
from worksheet1 import *

# DO NOT CHANGE ANYTHING IN THIS FILE

class TestBasicOperators(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 7), 11)
        self.assertEqual(add(-4, 7), 3)


    def test_subt(self):
        self.assertEqual(subt(4, 7), -3)
        self.assertEqual(subt(-4, 7), -11)

    def test_mult(self):
        self.assertEqual(mult(4, 7), 28)
        self.assertEqual(mult(-4, 2), -8)

    def test_div(self):
        self.assertEqual(div(8, 4), 2)
        self.assertEqual(div(8, 0), 0)

    def test_and(self):
        self.assertEqual(and_gate(True, True), True)
        self.assertEqual(and_gate(False, False), False)
        self.assertEqual(and_gate(False, True), False)
        self.assertEqual(and_gate(True, False), False)

    def test_or(self):
        self.assertEqual(or_gate(True, True), True)
        self.assertEqual(or_gate(False, False), False)
        self.assertEqual(or_gate(False, True), True)
        self.assertEqual(or_gate(True, False), True)

    def test_xor(self):
        self.assertEqual(xor_gate(True, True), False)
        self.assertEqual(xor_gate(False, False), False)
        self.assertEqual(xor_gate(False, True), True)
        self.assertEqual(xor_gate(True, False), True)

if __name__ == '__main__':
    unittest.main()
