# House Price Prediction

This project is inspired by the [Machine Learning project list](https://docs.google.com/document/d/1-CQHiW1V2yzZB0NS2lOPA8A7udNoUF8p884Q14J13q8/mobilebasic). The goal is to build a regression model to predict house prices based on features like size, location, and number of rooms.

## Table of Contents
- [Previous Configurations](#previous-configurations)
- [EDA](#eda)
- [Feature Engineering](#feature-engineering)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Previous Configurations

In order to run this script, you will need:

- The necessary libraries installed
- A `.env` file with the required environment variables
- Input files obtained from the original source: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data?select=data_description.txt)

### Installing the Libraries

The script works with the following versions:
- python `3.11.5`
- pandas `2.1.0`
- numpy `1.25.2`
- matplotlib `3.7.2`
- python-dotenv `1.0.0`
- scikit-learn `1.3.0`
- seaborn `0.12.2`
- scipy `1.11.2`

To install the necessary libraries, run:
```sh
pip install -r requirements.txt
```

### Environmental Variables

The `.env` file should include:
```sh
TEST_DATA="data/input/test.csv"
TRAIN_DATA="data/input/train.csv"
```

## EDA

Several columns have missing values. To handle this:
- Categorical features are filled with `'None'`.
- Numerical features are filled with `0`.
- Outliers were detected and handled by capping extreme values.

## Feature Engineering

- **Scaling**: Numerical features are standardized using MinMaxScaler.
- **Encoding**: One-hot encoding is applied to categorical features.

## Model

Our regression model underwent multiple refinements:
- **Initial Attempts**: Standard linear regression performed well but was improved further.
- **Outlier Handling**: Improved model performance by reducing high residual errors.
- **Feature Selection via PCA**: Helped in reducing multicollinearity and optimizing performance.
- **Final Performance Metrics**:
  - **Validation MSE**: 583,198,692.8265
  - **Validation R²**: 0.8889

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
