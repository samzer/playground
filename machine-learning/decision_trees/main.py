from base import DecisionTree, read_data, precision, recall
import numpy as np

data = read_data('../data/titanic.csv')

Y = [float(e[0]) for e in data]
X = [[ float(e) for e in row[1:]] for row in data]

model = DecisionTree(30,6)
model.fit(X, Y)

y_pred = model.predict(X)
print(f"Precision = {precision(Y, y_pred)} Recall = {recall(Y, y_pred)}" )
