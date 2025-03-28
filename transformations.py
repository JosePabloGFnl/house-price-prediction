import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

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
    
    def feature_preparation(self):
        preprocessor = ColumnTransformer(
        transformers=[
                ('num', StandardScaler(), self.numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), self.categorical_features)
            ]
        )

        X_transformed = preprocessor.fit_transform(self.data)

        columns = (
            self.numerical_features +
            list(preprocessor.named_transformers_['cat'].get_feature_names_out(self.categorical_features))
        )

        X_transformed = pd.DataFrame(X_transformed, columns=columns)

        return X_transformed
