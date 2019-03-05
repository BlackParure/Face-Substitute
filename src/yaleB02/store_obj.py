import pickle
from albedo_recover import *

def dump_it(obj, path):
    f = open(path, "wb")
    pickle.dump(obj, f)
    f.close()

def load_it(path):
    f = open(path, "rb")
    data = pickle.load(f)
    f.close()
    return data

if __name__ == "__main__":
    path = r"D:\library\python\opencv\04\depth.pickle"
    depth = get_f(cache_images_yaleB01())
    print(depth.shape)
    dump_it(depth, path)
