from sklearn.linear_model import LogisticRegression
from base import MultipleLogisticRegression, feature_scale, read_data
from sklearn.datasets import load_iris
import numpy as np

data = read_data('titanic.csv')
Y = [float(e[0]) for e in data]
X = [[ float(e) for e in row[1:]] for row in data]
X = np.array(X)
X = feature_scale(X, -1, 1)

model = MultipleLogisticRegression(epoch=20000, lr=0.001, batch_size=40)
model.fit(X, Y)

print('----LogisticRegression----')
print(f'Weight: {model.weight} Bias: {model.bias}')
print('\n')

sklearn_model = LogisticRegression()
sklearn_model.fit(X,Y)
print('----Sklearn LogisticRegression----')
print(f'Weight: {sklearn_model.coef_} Bias: {sklearn_model.intercept_}')
