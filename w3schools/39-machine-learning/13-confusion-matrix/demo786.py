# W3Schools, Python Machine Learning, Confusion Matrix
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size = 1000)
predicted = numpy.random.binomial(1, .9, size = 1000)

Accuracy = metrics.accuracy_score(actual, predicted)
Precision = metrics.precision_score(actual, predicted)
Sensitivity_recall = metrics.recall_score(actual, predicted)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)
F1_score = metrics.f1_score(actual, predicted)

# metrics:
print({
    "Accuracy": Accuracy,
    "Precision": Precision,
    "Sensitivity_recall": Sensitivity_recall,
    "Specificity": Specificity,
    "F1_score": F1_score
})
