# W3Schools, Python Machine Learning, Confusion Matrix
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1, .9, size = 1000)
predicted = numpy.random.binomial(1, .9, size = 1000)

Specificity = metrics.recall_score(actual, predicted, pos_label=0)

print(Specificity)
