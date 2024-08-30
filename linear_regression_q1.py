# Import libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import argparse

class MyLinearRegression:
    def __init__(self, test_set_path):
        self.X = None
        self.y = None
        self.y_true = None
        self.X_test = None
        self.model = None
        self.test_set_path = test_set_path

    def read_csv(self):
        self.training_set = pd.read_csv('training_q1.csv', sep=',', header=0, encoding = 'utf-8')
        self.test_set = pd.read_csv(self.test_set_path, sep=',', header=0, encoding = 'utf-8')

    def model_fit(self):
        # Fit LinearRegression model here
        pass
        
    def data_cleaning(self):
        # No data cleaning required for question 1
        pass
    
    def train(self):
        self.read_csv()
        self.data_cleaning()
        self.model_fit()
    
    def model_predict(self):
        '''
        Calculate the accuracy of the algorithm on the test set and returns 
        the coefficient of determination of the prediction.
        '''
        self.train()
        assert self.model is not None, "Initialize the model, i.e. fill in and run the model_fit function"
        r_score = 0
        return r_score


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Linear Regression')
    parser.add_argument('--test_dataset', type=str, default = "test.csv", help='path to test dataset')
    args = parser.parse_args()
    classifier = MyLinearRegression(args.test_dataset)
    acc = classifier.model_predict()
    print("Accuracy: ", acc)