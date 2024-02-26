import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:
    def __init__(self, num_layers, activation=sigmoid):
        self.num_layers = num_layers
        self.activation = activation

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

    def feed_forward(self, a_in, weights_arrays):
        output = self.start_with_one(a_in)
        for i in range(self.num_layers):
            a_out = self.dense(output, weights_arrays[i], self.activation)
            output = self.start_with_one(a_out)
        output = output[1:]
        self.output = output
        return output
