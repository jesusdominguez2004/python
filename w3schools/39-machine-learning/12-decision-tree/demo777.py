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

tree.plot_tree(dtree, feature_names=features)
plt.show()
