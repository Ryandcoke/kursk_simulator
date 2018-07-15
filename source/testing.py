import unittest
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
        self.assertEquals(1, self.rack.get_shell_count())

    def test_get_shell_count_2(self):
        self.rack.add("b")
        self.assertEquals(2, self.rack.get_shell_count())

if __name__ == '__main__':
    unittest.main()
