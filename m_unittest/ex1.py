# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase

__author__ = 'JiaweiMao'
__version__ = '1.0.0'


class TestStringMethods(TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.plit fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
