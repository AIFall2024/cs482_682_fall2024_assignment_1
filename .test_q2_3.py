#!/usr/bin/env python3
from linear_regression_q2 import MyLinearRegression
import unittest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class TestMyLinearRegression(unittest.TestCase):

    def test_basic_play_game_1(self):
        classifier = MyLinearRegression('dataset_q2.csv')
        acc = classifier.model_predict()
        acc = acc*100.0
        print("Your accuracy= {}%".format(acc))
        self.assertTrue(acc >= 4.0)

if __name__ == '__main__':
    unittest.main()