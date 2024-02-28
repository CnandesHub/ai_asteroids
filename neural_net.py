import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:
    def __init__(self, arr_size_layers, activation=sigmoid):
        self.arr_size_layers = arr_size_layers
        self.activation = activation
        self.arr_weight_layers = []

    @staticmethod
    def start_with_one(arr):
        new_size = arr.size + 1
        new_arr = np.empty(new_size)
        new_arr[0] = 1
        new_arr[1:] = arr
        return new_arr

    @staticmethod
    def dense(a_in, W, activation):
        z = np.matmul(W, a_in)
        a_out = activation(z)
        return a_out

    def feed_forward(self, a_in):
        output = a_in
        for i in range(len(self.arr_size_layers) - 1):
            a_out = self.dense(output, self.arr_weight_layers[i], self.activation)
            output = a_out
        self.output = output
        return output

    def set_weights(self, weights):
        self.arr_weight_layers = weights
