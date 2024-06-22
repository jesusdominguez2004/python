# W3Schools, Python Machine Learning, Logistic Regression
import numpy
from sklearn import linear_model

# X represents the size of a tumor in centimeters.
# Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
# y represents whether or not the tumor is cancerous (0 for "No", 1 for "Yes").
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)

log_odds = logr.coef_
odds = numpy.exp(log_odds)

def logit2prob(logr, X):
    log_odds = logr.coef_ * X + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds / (1 + odds)
    return (probability)

print(logit2prob(logr, X))

"""
odds is 4.03541657
This tells us that as the size of a tumor increases by 1mm 
the odds of it being a cancerous tumor increases by 4x.

3.78 0.61 The probability that a tumor with the size 3.78cm is cancerous is 61%.
2.44 0.19 The probability that a tumor with the size 2.44cm is cancerous is 19%.
2.09 0.13 The probability that a tumor with the size 2.09cm is cancerous is 13%.
...
"""
