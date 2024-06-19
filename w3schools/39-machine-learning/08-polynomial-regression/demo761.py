# W3Schools, Python Machine Learning, Polynomial Regression
import numpy
from sklearn.metrics import r2_score

# An example where polynomial regression 
# would not be the best method to predict future values.
x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# 0.00995 indicates a very bad relationship, 
# and tells us that this data set is not suitable 
# for polynomial regression.
print(r2_score(y, mymodel(x)))
