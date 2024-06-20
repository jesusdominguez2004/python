# W3Schools, Python Machine Learning, Train/Test
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

# The x axis represents the number of minutes before making a purchase
# The y axis represents the amount of money spent on the purchase
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# The training set should be a random selection of 80% of the original data.
# The testing set should be the remaining 20%.
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# Display the Training Set
plt.scatter(train_x, train_y)
plt.show()
