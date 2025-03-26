# House Price Prediction

## Table of Contents
- [Previous Configurations](#previous-configurations)
- [EDA](#eda)
- [FE](#fe)
- [Model](#model)
- [Procedure](#procedure)
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

- ``: 

Your `.env` file should look like this:

``` textplain

```

### Input data

The input data that used is from 

- ``: 

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


## FE

## Model

## Procedure

1. **Import Libraries**:
    ```python

    ```

2. **Set Environment Variables**:


3. **Validate Environment Variables**:
    Check if the environment variables are set and raise an error if they are not:
    ```python

    ```

4. **Check File Existence**:
    Verify that the file exists at the specified path:
    ```python

    ```

5. **Load Data**:
    Load the data from the specified Excel file and sheet into a pandas DataFrame:
    ```python

    ```

6. **Data Preprocessing**:
    Perform necessary data preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features:
    ```python

    ```

7. **Train-Test Split**:
    Split the data into training and testing sets:
    ```python

    ```

8. **Model Training**:
    Train a machine learning model (e.g., Logistic Regression) on the training data:
    ```python

    ```

9. **Model Evaluation**:
    Evaluate the model on the testing data and print the classification report and confusion matrix:
    ```python

    ```

10. **Data Visualization**:
    Use `matplotlib` and `seaborn` to visualize the data and the results:
    ```python

    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
