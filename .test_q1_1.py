#!/usr/bin/env python3
from linear_regression_q1 import MyLinearRegression
import unittest
import numpy as np

class TestMyLinearRegression(unittest.TestCase):

    def test_basic_play_game_1(self):
        classifier = MyLinearRegression('test_q1.csv')
        acc = classifier.model_predict()
        acc = acc*100.0
        print("Your accuracy= {}%".format(acc))
        self.assertTrue(acc >= 75.)

if __name__ == '__main__':
    unittest.main()