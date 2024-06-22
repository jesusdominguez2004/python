# W3Schools, Python Machine Learning, Categorical Data
import pandas
from sklearn import linear_model

cars = pandas.read_csv("data.csv")
ohe_cars = pandas.get_dummies(cars[['Car']])

X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X,y)

# predict the CO2 emission of a Volvo 
# where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

print(predictedCO2)

"""
- For each column, the values will be 1 or 0 
- where 1 represents the inclusion of the group 
- and 0 represents the exclusion. 
- This transformation is called one hot encoding.
- A column was created for every car brand in the Car column.
"""
