import numpy as np


def start_with_one(arr):
    new_size = arr.size + 1
    new_arr = np.empty(new_size)
    new_arr[0] = 1
    new_arr[1:] = arr
    return new_arr


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def dense(a_in, W, activation):
    z = np.matmul(W, a_in)
    a_out = activation(z)
    return a_out


def neural_net(a_0, W_0, W_1, W_2):
    a_1 = dense(a_0, W_0, sigmoid)
    a_2 = dense(a_1, W_1, sigmoid)
    a_3 = dense(a_2, W_2, sigmoid)
    return start_with_one(a_3)
