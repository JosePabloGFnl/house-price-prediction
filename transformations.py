import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Transformations:
    def __init__(self, data, categorical_features, numerical_features):
        self.data = data
        self.categorical_features = categorical_features
        self.numerical_features = numerical_features

    def null_handler(self):
        for col in self.categorical_features:
            self.data[col].fillna("None", inplace=True)

        for col in self.numerical_features:
            self.data[col].fillna(0, inplace=True)
        return self.data