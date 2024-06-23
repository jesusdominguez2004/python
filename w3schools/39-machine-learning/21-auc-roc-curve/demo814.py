# W3Schools, Python Machine Learning, AUC - ROC Curve
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

n = 10000
ratio = .95
n_0 = int((1 - ratio) * n)
n_1 = int(ratio * n)

y = np.array([0] * n_0 + [1] * n_1)
y_prob_2 = np.array(
    np.random.uniform(0, .7, n_0).tolist() +
    np.random.uniform(.3, 1, n_1).tolist()
)
y_pred_2 = y_prob_2 > .5

print(f'accuracy score: {accuracy_score(y, y_pred_2)}')
cf_mat = confusion_matrix(y, y_pred_2)
print('Confusion matrix')
print(cf_mat)
print(f'class 0 accuracy: {cf_mat[0][0] / n_0}')
print(f'class 1 accuracy: {cf_mat[1][1] / n_1}')

"""
- y_prob_2 and y_pred_2 are the probabilities 
- obtained from a hypothetical model 
- that doesn't always predict the mode
"""
