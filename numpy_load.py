import numpy as np

with np.load("KMNIST/kmnist-test-imgs.npz") as data:
    for i in data['arr_0']:
        print(i.shape)
with np.load("KMNIST/kmnist-test-labels.npz") as data:
    for i in data['arr_0']:
        print(i.shape)
with np.load("KMNIST/kmnist-train-imgs.npz") as data:
    for i in data['arr_0']:
        print(i.shape)
with np.load("KMNIST/kmnist-train-labels.npz") as data:
    for i in data['arr_0']:
        print(i.shape)


