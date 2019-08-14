import csv
import numpy as np
from collections import Counter


class DecisionTree:
    def __init__(self, max_depth, min_split_size):
        self.max_depth = max_depth
        self.min_split_size = min_split_size
        self.tree = {}

    def fit(self, X, Y):
        data = self.combine_XY(X, Y)
        self.tree = self.create_node(data)
        self.create_branch(self.tree, 1)

    def create_branch(self, node, depth):
        if not node['left'] or not node['right']:
            node['left'] = node['right'] = self.create_leaf(node['left'] + node['right'])
            return

        if depth >= self.max_depth:
            node['left'] = self.create_leaf(node['left'])
            node['right'] = self.create_leaf(node['right'])
            return

        if len(node['left']) > self.min_split_size:
            node['left'] = self.create_node(node['left'])
            self.create_branch(node['left'], depth + 1)
        else:
            node['left'] = self.create_leaf(node['left'])

        if len(node['right']) > self.min_split_size:
            node['right'] = self.create_node(node['right'])
            self.create_branch(node['right'], depth + 1)
        else:
            node['right'] = self.create_leaf(node['right'])


    def gini_index(self, data_groups):
        # Get the number of classes
        N = float(sum([ len(group) for group in data_groups]))
        gini_index = 0.0

        # Iterate through the groups
        for group in data_groups:
            # Get the proportion for each class
            group_size = float(len(group))

            if group_size == 0:
                continue

            class_counts =  Counter([row[-1] for row in group])

            p_square = 0.0
            for c in class_counts:
                p = class_counts[c]/group_size
                p_square += p*p

            gini_index += (1 - p*p)*( group_size/N)

        return gini_index

    def predict(self, x):
        result = list()

        for row in x:
            prediction = self.predict_single(row)
            result.append(prediction)

        return result

    def predict_single(self, data, node=None):
        node =  node if node else  self.tree

        if data[node['col_index']] < node['split_value']:
            if isinstance(node['left'], dict):
                return self.predict_single(data, node['left'] )
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.predict_single(data, node['right'] )
            else:
                return node['right']

    def create_node(self, data):
        gini_index = float('inf')
        split_value = None
        col_index = None
        left = None
        right = None

        num_row = len(data)
        num_col = len(data[0]) - 1

        # Iterate through columns
        for c in range(num_col):

            # Iterate through the rows
            for r in range(num_row):
                # Find the gini_index of that split
                data_groups = self.split_data(data, c, data[r][c])

                current_gini = self.gini_index(data_groups)

                # If the gini_index is less than the current gini_index then track the split_value, index and gini_index
                if current_gini < gini_index:
                    gini_index = current_gini
                    split_value = data[r][c]
                    col_index = c
                    left = data_groups[0]
                    right = data_groups[1]

        return {
                'col_index': col_index
                ,'split_value': split_value
                ,'left': left
                ,'right': right
                }

    def split_data(self, data, col_index, value):
        left = list()
        right = list()

        for row in data:
            if row[col_index] < value:
                left.append(row)
            else:
                right.append(row)

        return left, right

    def create_leaf(self, data):
        classes = [ row[-1] for row in data]

        # Count the instance of each classes
        class_counts = Counter(classes)

        # return the class with the maximum count
        result = max(set(classes), key=lambda c: class_counts[c])

        return result

    def combine_XY(self, X, Y):
        data = X[:]

        for i, row in enumerate(data):
            row.append(Y[i])

        return data

    #TODO
    def information_gain(self):
        pass

    #TODO
    def cross_entropy(self):
        pass

def read_data(filename):
    result = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            result.append(row)

    return result

def precision(y_actual, y_pred):
    if len(y_actual) != len(y_pred):
        raise ValueError("y_actual and y_pred need to be of same dimension")

    tp = 0
    fp = 0

    for i in range(len(y_pred)):
        if y_pred[i] == 0:
            continue

        if y_pred[i] == y_actual[i]:
            tp += 1
        else:
            fp += 1

    return tp/(tp + fp)

def recall(y_actual, y_pred):
    if len(y_actual) != len(y_pred):
        raise ValueError("y_actual and y_pred need to be of same dimension")

    tp = 0
    fn = 0

    for i in range(len(y_pred)):
        if y_actual[i] == 0:
            continue

        if y_pred[i] == y_actual[i]:
            tp += 1
        else:
            fn += 1

    return tp/(tp + fn)
