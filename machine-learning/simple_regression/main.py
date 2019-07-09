from base import SimpleLinearRegression, read_data
from sklearn.linear_model import LinearRegression

data = read_data('data.csv')
Y = [float(e[1]) for e in data]
X = [float(e[0]) for e in data]

model = SimpleLinearRegression(epoch=80000, lr=0.0001, batch_size=18)
model.fit(X, Y)

print('----SimpleLinearRegression----')
print(f'Weight: {model.weight} Bias: {model.bias}')
print('\n')

sklearn_model = LinearRegression()
sklearn_model.fit([ [e] for e in X],Y)
print('----Sklearn LinearRegression----')
print(f'Weight: {sklearn_model.coef_[0]} Bias: {sklearn_model.intercept_}')
