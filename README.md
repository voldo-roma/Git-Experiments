# Lending Club – Loan Default Prediction

*A Data Science in Finance Capstone Project – Dom Sileika*

##  Objective

The goal of this project is to develop a predictive model to assess credit risk for Lending Club applicants. By identifying potential defaults at the point of application, the business can improve approval decisions, reduce financial losses, and strengthen overall portfolio quality.

##  Dataset

Historical Lending Club loan application data (2007–2020), including:
- Loan features (amount, term, interest rate)
- Applicant demographics and financial details
- Final loan outcome (fully paid, charged off)

Target variable:
- `Charged Off` = 1 (default)
- `Fully Paid` = 0 (non-default)

##  Exploratory Analysis

- Significant class imbalance (approx. 85% fully paid, 15% charged off)
- Interest rates, loan amount, and DTI were slightly higher for defaulters
- Outliers were detected but not transformed, as tree-based models handle them robustly
- Features such as `emp_title` and `zip_code` were removed due to high cardinality or privacy concerns

> “Start simple. Then tune. Then test. But never skip the story behind your dataset.”  
> – Cassie Kozyrkov, Chief Decision Scientist @ Google

### Modelling Approach

Two models were compared:

| Model                    | Method            | Imbalance Strategy | Notes                     |
|-------------------------|-------------------|---------------------|---------------------------|
| Logistic Regression     | Linear baseline   | None                | Simple but weak recall    |
| Random Forest + SMOTE   | Ensemble          | Oversampling (SMOTE)| Stronger recall and AUC   |

Cross-Validation Results (5-fold ROC AUC for Logistic Regression):
[0.6907, 0.6855, 0.6873, 0.6888, 0.6869] Mean ROC AUC: 0.6879


Evaluation metrics:

| Model                 | Precision | Recall | F1 Score | ROC AUC |
|----------------------|-----------|--------|----------|---------|
| Logistic Regression  | 0.53      | 0.03   | 0.06     | 0.70    |
| Random Forest + SMOTE| 0.35      | 0.31   | 0.32     | 0.67    |

The enhanced model captures far more defaults, making it preferable for real-world deployment, especially considering the high cost of false negatives in credit decisions.

## Business Impact

- Improved risk classification before loan issuance
- Reduces long-term exposure to default risk
- Easily deployable via an API or lightweight interface (e.g. Streamlit)

## Technologies

- Python 3, pandas, scikit-learn, seaborn
- SMOTE (imbalanced-learn)
- Jupyter Notebook

---

## to Run
1. Clone the repository  
2. Install dependencies:
pip install pandas scikit-learn seaborn imbalanced-learn

📚 References
Kozyrkov, Cassie. @DecisionScientist
Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow
scikit-learn documentation: https://scikit-learn.org/
