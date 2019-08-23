from functools import reduce
import numpy as np


def mult_vect_scalar(data, scalar):
    return data[0]*scalar + data[1] * scalar


def adjust_w(w, est, res, data):
    err = (est+0) - (res + 0)
    merged = [data, err]
    return w + reduce(mult_vect_scalar, merged)


def adjust_b(b, est, res, etha): return b + etha * (est - res)


def act_fun(w, data, b):
    return np.dot(w, data) + b > 0


w = np.random.rand(4, 2)
b = np.random.rand()
etha = 0.5
results = [0, 0, 0, 1]

training_set = [
    [0, 1],
    [1, 0],
    [0, 0],
    [1, 1]


]
not_converge = True
idx = 0
while not_converge:
    y = act_fun(w[idx], training_set[idx], b)
    if y != results[idx]:
        w[idx] = adjust_w(w[idx], results[idx], y, training_set[idx])
        b = adjust_b(b, results[idx], y, etha)
    if idx+1 == len(training_set):
        print(w)
        print("\r")
        idx = 0
    idx += 1
