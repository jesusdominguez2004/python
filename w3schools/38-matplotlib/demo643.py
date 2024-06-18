# W3Schools, Python Matplotlib, Markers
import matplotlib.pyplot as plt
import numpy as np

# The x-points in the example are [0, 1, 2, 3, 4, 5]
ypoints = np.array([3, 8, 1, 10])

# This parameter is also called fmt 'marker|line|color'
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()