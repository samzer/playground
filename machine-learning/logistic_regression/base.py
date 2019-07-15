import csv
import numpy as np


class MultipleLogisticRegression:
    def __init__(self, epoch=3, batch_size=15, lr=0.001):
        self.weight = []
        self.bias = 0
        self.epoch = epoch
        self.batch_size = batch_size
        self.lr = lr

    def fit(self, X, Y):
        num_batch = len(X)//self.batch_size + 1
        self.weight = np.zeros((len(X[0])))

        for i in range(self.epoch):
            for j in range(num_batch):
                self.update_weights(X[j*self.batch_size: (j+1)*self.batch_size]
                                    ,Y[j*self.batch_size: (j+1)*self.batch_size])

    def sgd(self, x_batch, y_batch):
        dCw = np.zeros((self.weight.shape[0]))
        dCb = 0
        bs = len(x_batch)

        y_pred = self.predict(x_batch)
        y_actual = y_batch
        diff = y_pred - y_actual

        dCw = np.dot(np.transpose(x_batch), diff)
        dCb =  sum(diff)

        dCw = dCw/bs
        dCb = dCb/bs

        self.weight -=  self.lr * dCw
        self.bias -=  self.lr * dCb

    def cost(self, X, Y):
        y_pred = self.predict(X)
        N = len(Y)
        cost_sum = np.sum((Y*np.log(y_pred) + (1-Y)*np.log(1 - y_pred)) , axis=0)

        return -(cost_sum / N)

    def update_weights(self, x_batch, y_batch):
        self.sgd(x_batch, y_batch)

    def predict(self, x):
        return 1/(1 + np.exp(- (np.dot(x, self.weight) + self.bias)))


def feature_scale(X, x_min, x_max):
    nom = (X-X.min(axis=0))*(x_max-x_min)
    denom = X.max(axis=0) - X.min(axis=0)
    denom[denom==0] = 1
    return x_min + nom/denom

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
