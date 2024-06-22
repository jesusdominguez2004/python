# W3Schools, Python Machine Learning, Categorical Data
import pandas as pd

cars = pd.read_csv('data.csv')
ohe_cars = pd.get_dummies(cars[['Car']])

print(ohe_cars.to_string())

"""
- For each column, the values will be 1 or 0 
- where 1 represents the inclusion of the group 
- and 0 represents the exclusion. 
- This transformation is called one hot encoding.
- A column was created for every car brand in the Car column.
"""
