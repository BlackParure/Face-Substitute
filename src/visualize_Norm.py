import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pickle

def load_it(path):
    f = open(path, "rb")
    data = pickle.load(f)
    f.close()
    return data

norm_path = r"D:\library\python\opencv\04\norm.pickle"
n = load_it(norm_path)
width = 168
height = 192

n_x = np.zeros((width, height))
n_y = np.zeros((width, height))
n_z = np.zeros((width, height))
for x in range(width):
    for y in range(height):
        n_x[x, y] = n[x, y, 0]
        n_y[x, y] = n[x, y, 1]
        n_z[x, y] = n[x, y, 2]

ax = plt.subplot(131)
ax.imshow(n_x.T, cmap="jet")
ax = plt.subplot(132)
ax.imshow(n_y.T, cmap="jet")
ax = plt.subplot(133)
ax.imshow(n_z.T, cmap="jet")
plt.show()

