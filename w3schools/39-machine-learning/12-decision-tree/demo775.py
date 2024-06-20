# W3Schools, Python Machine Learning, Decision Tree
import pandas

df = pandas.read_csv("data.csv")

# To make a decision tree, all data has to be numerical
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)

d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)
