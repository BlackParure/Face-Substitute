import numpy as np
from load_images import *
from PIL import Image


def aek2V(azimuth, elevation, max_intensity):
    e = elevation / 180 * np.pi
    a = azimuth / 180 * np.pi
    x = np.cos(e) * np.sin(a) * max_intensity
    y = np.sin(e) * max_intensity
    z = np.cos(e) * np.cos(a) * max_intensity

    output = np.array([x, y, z])
    return output

def get_V_pinv(images):
    n = len(images) - 1
    V_matrix = np.zeros((n, 3))
    index = 0
    for image in images:
        if image.img_type == "Non-Ambient":
            V_matrix[index] = aek2V(image.azimuth, image.elevation, 255)
            index += 1

    return np.linalg.pinv(V_matrix)

def get_I_x_y(x, y, images):
    n = len(images) - 1
    output = np.zeros((n, 1))
    index = 0
    for image in images:
        if image.img_type == "Non-Ambient":
            output[index, 0] = image[x, y]
            index += 1
        else:
            output[:, 0] -= image[x, y]

    return output

def get_g_x_y(x, y, images, V_pinv):
    """

    :param x:
    :param y:
    :param images:
    :param V_pinv: readin V_pinv to avoid the waste of resources
    :return:
    """
    I_x_y = get_I_x_y(x, y, images)
    output = np.matmul(V_pinv, I_x_y).reshape(3,)

    return output

def get_g(images):
    x_min = 0
    x_max = 167
    y_min = 0
    y_max = 191

    V_pinv = get_V_pinv(images)

    width = x_max - x_min + 1
    height = y_max - y_min + 1
    output = np.zeros((width, height, 3))
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            output[x, y] = get_g_x_y(x, y, images, V_pinv)

    return output

def get_albedo(images):
    g = get_g(images)
    width = 168
    height = 192
    output = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            output[x, y] = np.linalg.norm(g[x, y])
    return output * 255

def get_N(images):
    g = get_g(images)
    width = 168
    height = 192
    output = np.zeros((width, height, 3))
    for x in range(width):
        for y in range(height):
            output[x, y] = g[x, y] / np.linalg.norm(g[x, y])
    return output


def save_albedo_colored_sized(width, height):
    images = cache_images_yaleB01()
    albedo = get_albedo(images)
    height = int(height)
    width = int(width)
    path_albedo = r"D:\library\python\opencv\04\albedo.png"
    image_albedo = Image.fromarray(albedo).convert("L")
    image_albedo.save(path_albedo)
    cv2_image = cv2.imread(path_albedo)
    cv2_image_resized = cv2.resize(cv2_image,(height, width),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(path_albedo, cv2_image_resized)

def save_albedo_colored_sized(width, height, num):
    images = cache_images_yale(num)
    albedo = get_albedo(images)
    height = int(height)
    width = int(width)
    path_albedo = r"D:\library\python\opencv\04\albedo.png"
    image_albedo = Image.fromarray(albedo).convert("L")
    image_albedo.save(path_albedo)
    cv2_image = cv2.imread(path_albedo)
    cv2_image_resized = cv2.resize(cv2_image,(height, width),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(path_albedo, cv2_image_resized)

def get_f(images):
    g = get_g(images)
    width = 168
    height = 192
    f_x = g[:,:,0]/g[:,:,2]
    f_y = g[:,:,1]/g[:,:,2]
    f = np.zeros((width, height))
    for y in range(1, height):
        f[0, y] = f[0, y-1] + f_y[0, y-1]

    for x in range(1, width):
        for y in range(0, height):
            f[x, y] = f[x-1, y] + f_x[x-1, y]

    return f

if __name__ == "__main__":
    save_albedo_colored_sized(168 / 2, 192 / 2)
