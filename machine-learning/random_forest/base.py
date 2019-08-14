from decision_tree import DecisionTree
from random import randrange, sample
from math import sqrt
from statistics import mean

class RandomForest:
    def __init__(self, max_depth, min_split_size, sample_ratio, num_trees, num_features=None):
        self.trees = list()
        self.max_depth = max_depth
        self.min_split_size = min_split_size
        self.sample_ratio = sample_ratio
        self.num_trees = num_trees
        self.num_features = num_features

    def fit(self,X, Y):
        if not self.num_features:
            self.num_features = round(sqrt(len(X[0])))

        # Iterate through number of num_trees
        for t in range(self.num_trees):
            # Get the sample data
            x, y, col_indexes = self.get_sample_data(X,Y)

            # Create the tree and append to the list
            tree = DecisionTree(self.max_depth, self.min_split_size)
            tree.fit(x, y, col_indexes)

            self.trees.append(tree)

    def get_sample_data(self, X, Y):
        x = list()
        y = list()

        # Get the sample of data with replacements
        num_samples = round(len(X) * self.sample_ratio)

        for i in range(num_samples):
            row_index = randrange(num_samples)
            x.append(X[row_index])
            y.append(Y[row_index])

        # Get the subset of features indexes
        col_indexes = sample([ i for i in range(len(X[0]))], self.num_features)

        return x, y, col_indexes

    def predict(self, X):
        result = list()

        for row in X:
            result.append(self.predict_single(row))

        return result

    def predict_single(self, x):
        return round(mean([ t.predict_single(x) for t in self.trees ]))
