# W3Schools, Python Machine Learning, AUC - ROC Curve
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

n = 10000
ratio = .95
n_0 = int((1 - ratio) * n)
n_1 = int(ratio * n)

y = np.array([0] * n_0 + [1] * n_1)
y_prob = np.array([1] * n)
y_pred = y_prob > .5

print(f'accuracy score: {accuracy_score(y, y_pred)}')
cf_mat = confusion_matrix(y, y_pred)
print('Confusion matrix')
print(cf_mat)
print(f'class 0 accuracy: {cf_mat[0][0] / n_0}')
print(f'class 1 accuracy: {cf_mat[1][1] / n_1}')

"""
- y_prob and y_pred are the probabilities obtained from a hypothetical model 
- that always predicts the majority class
- probability of predicting class 1 is going to be 100%
"""
