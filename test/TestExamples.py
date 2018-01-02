'''
Created on 29.12.2017

@author: CorneliaCFranke
'''
import unittest
from src.examples import flaecheninhalt_quadrat


class TestExamples(unittest.TestCase):


    def test_flaecheninhalt(self):
        laenge = 2
        breite = 3
        actual = flaecheninhalt_quadrat(laenge, breite)
        self.assertEqual(6, actual, "Falscher Flaecheninhalt")