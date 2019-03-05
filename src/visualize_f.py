import pickle
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png

def dump_it(obj, path):
    f = open(path, "wb")
    pickle.dump(obj, f)
    f.close()

def load_it(path):
    f = open(path, "rb")
    data = pickle.load(f)
    f.close()
    return data

depth = load_it("D:\\library\\python\\opencv\\04\\depth.pickle")
print(depth.shape)
depth = depth[::2, ::2]

x, y = np.mgrid[0:168:2, 0:192:2]

fn = get_sample_data("D:\\library\\python\\opencv\\04\\albedo.png", asfileobj=False)
img = read_png(fn)

ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,depth,rstride=2,cstride=1,cmap=plt.cm.coolwarm,facecolors=img)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
