from random_forest import RandomForest
from decision_tree import read_data, precision, recall

data = read_data('data/titanic.csv')

Y = [float(e[0]) for e in data]
X = [[ float(e) for e in row[1:]] for row in data]

model = RandomForest(5, 4, 0.8 ,60, 2)
model.fit(X, Y)

y_pred = model.predict(X)
print(f"Precision = {precision(Y, y_pred)} Recall = {recall(Y, y_pred)}" )
