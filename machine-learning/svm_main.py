from support_vector_machine import SupportVectorMachine
from decision_tree import read_data, precision, recall

# X = [[1,2],
#         [1,1],
#         [2,5],
#         [1,4],
#         [5,6],
#         [7,2],
#         [8,3]]
#
# Y = [-1,
#      -1,
#      -1,
#       1,
#       1,
#       1,
#       1]

data = read_data('data/titanic.csv')
Y = [float(e[0]) for e in data]
X = [[ float(e) for e in row[1:]] for row in data]

model = SupportVectorMachine(1000)
model.fit(X, Y)

y_pred = model.predict(X)
print(y_pred)
print(f"Precision = {precision(Y, y_pred)} Recall = {recall(Y, y_pred)}" )
