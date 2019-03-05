import pickle
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from matplotlib.cbook import get_sample_data
from matplotlib._png import read_png
from albedo_recover import *

num = 2
images = cache_images_yale(num)
print("images cache complete")
depth = get_f(images)
print("depth complete")
depth = depth[::2, ::2]
save_albedo_colored_sized(168 / 2, 192 / 2, num)
print("albedo complete")

x, y = np.mgrid[0:168:2, 0:192:2]

fn = get_sample_data("D:\\library\\python\\opencv\\04\\albedo.png", asfileobj=False)
img = read_png(fn)

ax=plt.subplot(111,projection='3d')
ax.plot_surface(x,y,depth,rstride=2,cstride=1,cmap=plt.cm.coolwarm,facecolors=img)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
