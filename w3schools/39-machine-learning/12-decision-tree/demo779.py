# W3Schools, Python Machine Learning, Decision Tree
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

df = pandas.read_csv("data.csv")

# 1. To make a decision tree, all data has to be numerical
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)

d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# 2. feature columns and target column
features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

# 3. Create the actual decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Predict Values:
# Should I go see a show starring a 40 years old American comedian, 
# with 10 years of experience, and a comedy ranking of 6?
print(dtree.predict([[40, 10, 6, 1]]))
print("[1] means 'GO'")
print("[0] means 'NO'")
