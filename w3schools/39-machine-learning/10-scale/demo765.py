# W3Schools, Python Machine Learning, Scale
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

# z = (x - u) / s
scaledX = scale.fit_transform(X)
print(scaledX)
