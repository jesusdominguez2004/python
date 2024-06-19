# W3Schools, Python Machine Learning, Multiple Regression
import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])
print(predictedCO2)

"""
- The result array represents the coefficient values of weight and volume.
- Weight: 0.00755095
- Volume: 0.00780526
- These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
- And if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.

- We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.
- Which shows that the coefficient of 0.00755095 is correct:
- 107.2087328 + (1000 * 0.00755095) = 114.75968
"""
