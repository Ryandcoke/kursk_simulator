"""
Test suite for the entire program. Run this to execute all test cases.
Do not import this from other modules.
"""


import unittest

from util import time_function, time_class
import tanks
import tank_components
import shells


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestAmmoRack(unittest.TestCase):

    def setUp(self):
        self.rack = tank_components.AmmoRack(2, {"a": 1})

    def test_remove_1_key_True(self):
        self.assertTrue(self.rack.remove("a"))

    def test_remove_2_key_False(self):
        self.assertTrue(self.rack.remove("a"))
        self.assertFalse(self.rack.remove("a"))

    def test_remove_nokey_False(self):
        self.assertFalse(self.rack.remove("b"))

    def test_add_1_notFull_True(self):
        self.assertTrue(self.rack.add("a"))

    def test_add_2_full_False(self):
        self.assertFalse(self.rack.add("a", 2))

    def test_get_shell_count_1(self):
        self.assertEqual(1, self.rack.get_shell_count())

    def test_get_shell_count_2(self):
        self.rack.add("b")
        self.assertEqual(2, self.rack.get_shell_count())


class TestTankFactory(unittest.TestCase):

    # def test_get_tank_valid(self):
    #     sherman = tanks.TankFactory.get_tank(tanks.Tank.SHERMAN)
    #     self.assertEqual(5, sherman.speed)

    def test_get_tank_ValueError(self):
        with self.assertRaises(ValueError):
            tanks.TankFactory.get_tank("")


if __name__ == '__main__':
    unittest.main()
else:
    print("Do not import _test.py from other modules.")
