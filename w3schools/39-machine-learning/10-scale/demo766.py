# W3Schools, Python Machine Learning, Scale
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

# for each row: z = (x - u) / s
# z = (x - u) / s
# z = new value
# x = original value
# u = mean
# s = standard deviation
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

# Predict the CO2 emission 
# from a 1.3 liter car that weighs 2300 kilograms
scaled = scale.transform([[2300, 1.3]])

predictedC02 = regr.predict([scaled[0]])
print(predictedC02)
