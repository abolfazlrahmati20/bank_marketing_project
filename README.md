# Bank Marketing Prediction

## Introduction
This project uses Machine Learning to predict whether a bank customer will subscribe to a term deposit based on customer information and previous marketing campaign data.

The main goal is to identify potential customers who are more likely to accept the bank's offer.

## Dataset
The dataset used in this project is the Bank Marketing dataset.

It contains information about customers, including:

- Age
- Job
- Marital Status
- Education
- Balance
- Housing Loan
- Personal Loan
- Contact Type
- Campaign Information
- Previous Campaign Results

The target column is `y`:
- `0`: No
- `1`: Yes

## Data Preprocessing
The following preprocessing steps were performed:

- Checked missing values and duplicate records.
- Converted the target column into numerical values.
- Removed the `duration` column to prevent data leakage.
- Separated numerical and categorical features.
- Used Median Imputation and StandardScaler for numerical features.
- Used Most Frequent Imputation and OneHotEncoder for categorical features.
- Applied preprocessing using ColumnTransformer and Pipeline.

## Train and Test Split
The dataset was divided into:

- 80% Training Data
- 20% Testing Data

Stratified splitting was used to maintain the class distribution.

## Machine Learning Models
The following models were evaluated:

- K-Nearest Neighbors (KNN)
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

A DummyClassifier was also used as a baseline model.

## Model Evaluation
The models were evaluated using 5-fold Cross Validation.

The following metrics were considered:

- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC
- F2-score

Since the dataset is imbalanced and identifying potential customers is important, Recall was considered a priority.

## Hyperparameter Tuning
RandomizedSearchCV was used to find better hyperparameters.

The F2-score was selected as the optimization metric because it gives more importance to Recall than Precision.

## Final Model
Random Forest was selected as the final model after comparing the evaluated models and tuning their hyperparameters.

A decision threshold was also selected to achieve a Recall of at least 0.60 on the training validation predictions.

## Application
A Streamlit application was developed to make predictions using the trained model.

The application allows users to enter customer information and receive a prediction.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Conclusion
This project demonstrates how Machine Learning can be used to identify potential customers for bank marketing campaigns.

The main focus was on improving the identification of customers who are likely to subscribe to a term deposit, rather than relying only on Accuracy.