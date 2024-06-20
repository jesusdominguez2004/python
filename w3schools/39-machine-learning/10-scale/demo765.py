# W3Schools, Python Machine Learning, Scale
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

# for each row: z = (x - u) / s
# z = new value
# x = original value
# u = mean
# s = standard deviation
scaledX = scale.fit_transform(X)
print(scaledX)
