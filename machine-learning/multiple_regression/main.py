from sklearn.linear_model import LinearRegression
from base import MultipleLinearRegression, feature_scale
from sklearn.datasets import load_boston

data = load_boston()
Y = data['target']
X = data['data']
X = feature_scale(X, -1, 1)

model = MultipleLinearRegression(epoch=10000, lr=0.001, batch_size=20)
model.fit(X, Y)

print('----MultipleLinearRegression----')
print(f'Weight: {model.weight} Bias: {model.bias}')
print('\n')

sklearn_model = LinearRegression()
sklearn_model.fit( X,Y)
print('----Sklearn LinearRegression----')
print(f'Weight: {sklearn_model.coef_} Bias: {sklearn_model.intercept_}')
