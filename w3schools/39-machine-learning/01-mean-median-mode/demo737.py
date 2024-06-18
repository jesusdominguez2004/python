# W3Schools, Python Machine Learning, Mean Median Mode
from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(speed)   # the most common value

print(x)
