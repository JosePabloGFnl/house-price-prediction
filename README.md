# House Price Prediction

This project is inspired from the https://docs.google.com/document/d/1-CQHiW1V2yzZB0NS2lOPA8A7udNoUF8p884Q14J13q8/mobilebasic list of Machine Learning projects.
The goal is to build a regression model to predict house prices based on features like size, location, and number of rooms.

## Table of Contents
- [Previous Configurations](#previous-configurations)
- [EDA](#eda)
- [FE](#fe)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Previous configurations

In order to run this script, you will need:

- The necessary libraries installed
- Create .env file with the necessary environmental variables
- Obtain input files from the original source: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data?select=data_description.txt

### Installing the libraries

The script works with the following versions:
- python `3.11.5`
- pandas `2.1.0`
- numpy `1.25.2`
- matplotlib `3.7.2`
- python-dotenv `1.0.0`
- scikit-learn `1.3.0`
- Jinja2 `3.1.2`
- xlrd `2.0.1`

To install the necessary libraries, run the following code in a Python executer
``` CMD Commands
pip install python-dotenv
```

To view the version of your libraries, run the following:
``` CMD Commands
pip show python-dotenv
```

Another alternate method to view all of the installed libraries if the following:
``` CMD Commands
pip show list
```

An easier and quicker way to install is to run the following to install required packages:

``` CMD Commands
pip install -r requirements.txt
```

### Environmental variables

The `.env` file needs to have the following environmental variables for the script to work properly:

- `TEST_DATA`: Dataset containing 80 columns excluding the classified value `SalePrice` from the training set.
- `TRAIN_DATA`: Dataset containing the previously mentioned amount of columns and `SalePrice` as the classification value to be trained from.

Your `.env` file should look like this:

``` textplain
    TEST_DATA = "data\input\test.csv"
    TRAIN_DATA = "data\input\train.csv"
```

### Input data

The input data that used is from the House Prices - Advanced Regression Techniques dataset from Kaggle (https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data?select=data_description.txt). This source already divides the dataset into training and tests sets for us to utilize as well as descriptions for the columns.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/House-Price-Prediction.git
    cd House-Price-Prediction
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
    
## EDA
There's a large series of rows with missing data in several columns, we will fill categorical features with 'None' and numerical with '0' due to them not being feasible for removal or other Null Handling methods like filling with median.

## FE
Scaler for numerical features and One Hot Encoder for categorical features to fit the data.

## Model

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
