# W3Schools, Python Machine Learning, Percentile
import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# 90% of the people are:
x = numpy.percentile(ages, 90)

print(x)
