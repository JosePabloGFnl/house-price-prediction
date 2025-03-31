import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

class Transformations:
    def __init__(self, categorical_features, numerical_features):
        self.categorical_features = categorical_features
        self.numerical_features = numerical_features
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), self.categorical_features)
            ]
        )

    def null_handler(self, data):
        data = data.copy()  # Avoid modifying original DataFrame
        for col in self.categorical_features:
            data[col].fillna("None", inplace=True)
        for col in self.numerical_features:
            data[col].fillna(0, inplace=True)
        return data

    def fit_transform(self, data):
        data = self.null_handler(data)
        X_transformed = self.preprocessor.fit_transform(data)
        columns = (
            self.numerical_features +
            list(self.preprocessor.named_transformers_['cat'].get_feature_names_out(self.categorical_features))
        )
        return pd.DataFrame(X_transformed, columns=columns)

    def transform(self, data):
        data = self.null_handler(data)
        X_transformed = self.preprocessor.transform(data)
        columns = (
            self.numerical_features +
            list(self.preprocessor.named_transformers_['cat'].get_feature_names_out(self.categorical_features))
        )
        return pd.DataFrame(X_transformed, columns=columns)
