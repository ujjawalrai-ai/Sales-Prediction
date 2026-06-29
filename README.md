# Sales Prediction Using Linear Regression

## Overview

This project predicts product sales using a Linear Regression model. The objective is to analyze advertising data and build a machine learning system capable of predicting sales values based on advertising expenditures.

---

## Features

* Data visualization using Seaborn and Matplotlib
* Exploratory Data Analysis (EDA)
* Linear Regression model training
* Model evaluation using regression metrics
* Model saving using Pickle
* Interactive Streamlit dashboard
* Real-time sales prediction

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Pickle

---

## Dataset

The project uses the **Advertising dataset**, which contains advertising expenditure data and corresponding sales values.

The dataset:

* Contains only numerical features.
* Has no missing values.
* Does not require categorical encoding.
* Does not require feature scaling.

---

## Data Analysis and Visualization

The following visualizations and analyses were performed:

* Scatter plots using Matplotlib.
* Correlation analysis.
* Seaborn visualizations for understanding feature relationships.
* Exploratory Data Analysis to identify patterns in the dataset.

---

## Machine Learning Model

**Algorithm Used:** Linear Regression

The model was trained using Scikit-learn's Linear Regression algorithm to predict sales values.

---

## Model Performance

* R² Score: **0.8994**
* Mean Absolute Error (MAE): **1.46**

The model explains approximately **90% of the variance** in the sales data, indicating strong predictive performance.

---

## Project Workflow

1. Import the dataset.
2. Perform data visualization and analysis.
3. Split the dataset into training and testing sets.
4. Train the Linear Regression model.
5. Evaluate model performance using regression metrics.
6. Save the trained model using Pickle.
7. Build a Streamlit dashboard for predictions.

---

## Project Structure

Sales-Prediction/

├── Advertising.csv

├── Regression.ipynb

├── dashboard.py

├── linear_regression_model.pkl

├── Screenshot.png

├── requirements.txt

└── README.md

---

## Dashboard

The Streamlit dashboard allows users to:

* Enter advertising expenditure values.
* Predict sales in real time.
* Interact with a user-friendly interface.

---

## How to Run

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run dashboard.py
```

---

## Future Improvements

* Compare multiple regression algorithms.
* Deploy the application online.
* Add additional visualizations.
* Improve prediction performance with advanced models.

---

## Author

**Ujjawal Rai**
