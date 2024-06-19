# W3Schools, Python Machine Learning, Multiple Regression
import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

"""
- The result array represents the coefficient values of weight and volume.
- Weight: 0.00755095
- Volume: 0.00780526
- These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
- And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.
"""
