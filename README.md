# ELVTR - Data Science in Finance
## DSIF Assignment 3 – Challenger Model

###TL;DR
Built a better model, beat the baseline, logged the wins.

#DATASET
Lending Club loan application data from 2007 to 2020

### MODELS
- Baseline = Logistic Regression
- Challenger: Random Forest (100k sample, limited depth)

Trained Tuned Socred, compared performance side-by-side (ROC-AUC, F1, all that good stuff)

### CONCLUSION
Logistic Regression slightly outperformed Random Forest. Doesn't make RF worse, just in this setup the baseline was strong already - simplicity prevailed.


###### Stack
Python, scikit-learn, pandas, matplotlib. No drama.
