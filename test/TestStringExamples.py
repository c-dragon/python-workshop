'''
Created on 29.12.2017

@author: CorneliaCFranke
'''
import unittest
from src import stringExamples


class TestStringExamples(unittest.TestCase):


    def test_is_palindrom_returns_false_for_non_anagram(self):
        actual = stringExamples.is_palindrom("abc")
        self.assertEqual(False, actual)
        
    def test_is_palindrom_returns_true_for_anagram(self):
        self.assertEqual(True, stringExamples.is_palindrom("otto"))
        self.assertEqual(True, stringExamples.is_palindrom("anna"))