import csv


class SimpleLinearRegression:
    def __init__(self, epoch=3, batch_size=15, lr=0.001):
        self.weight = 0
        self.bias = 0
        self.epoch = epoch
        self.batch_size = batch_size
        self.lr = lr

    def fit(self, X, Y):
        num_batch = len(X)//self.batch_size + 1

        for i in range(self.epoch):
            for j in range(num_batch):
                self.update_weights(X[j*self.batch_size: (j+1)*self.batch_size]
                                    ,Y[j*self.batch_size: (j+1)*self.batch_size])

    def sgd(self, x_batch, y_batch):
        dCw = 0.0
        dCb = 0.0
        bs = len(x_batch)

        for i in range(bs):
            dCw +=  (self.weight*x_batch[i] + self.bias - y_batch[i])*x_batch[i]
            dCb +=  (self.weight*x_batch[i] + self.bias - y_batch[i])

        dCw = (2*dCw)/bs
        dCb = (2*dCb)/bs

        self.weight -=  self.lr * dCw
        self.bias -=  self.lr * dCb

        self.weight = clamp(self.weight, -500,500)
        self.bias = clamp(self.bias, -500,500)

    def cost(self, X, Y):
        y_pred = self.predict(X)
        N = len(Y)
        cost_sum = 0

        for i in range(N):
            cost_sum += (y_pred[i] - Y[i])**2

        return cost_sum / N

    def update_weights(self, x_batch, y_batch):
        self.sgd(x_batch, y_batch)

    def predict(self, x):
        return [ self.predict_single(e) for e in x]

    def predict_single(self, x_single):
        return self.weight*x_single + self.bias


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

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
