import pcl
import pcl.pcl_visualization
import numpy as np
import random


def main():
    cloud = pcl.load('data/lamppost.pcd')

    # параметры
    step = 2    # размер вокселя относительно облака
    rand_param = cloud.size // 2    # сколько точек отфильтровать

    arr = cloud.to_array().transpose()

    x_min = arr[0].min()
    x_max = arr[0].max()

    y_min = arr[1].min()
    y_max = arr[1].max()

    z_min = arr[2].min()
    z_max = arr[2].max()

    # координаты вокселей
    x_coords = []
    s = np.linspace(x_min, x_max, step)
    x_coords.append(s)
    s = np.linspace(y_min, y_min, step)
    x_coords.append(s)
    s = np.linspace(z_min, z_min, step)
    x_coords.append(s)

    y_coords = []
    s = np.linspace(x_min, x_min, step)
    y_coords.append(s)
    s = np.linspace(y_min, y_max, step)
    y_coords.append(s)
    s = np.linspace(z_min, z_min, step)
    y_coords.append(s)

    z_coords = []
    s = np.linspace(x_min, x_min, step)
    z_coords.append(s)
    s = np.linspace(y_min, y_min, step)
    z_coords.append(s)
    s = np.linspace(z_min, z_max, step)
    z_coords.append(s)

    coords = np.empty([3, step * 3])

    coords[0] = [*x_coords[0], *y_coords[0], *z_coords[0]]
    coords[1] = [*x_coords[1], *y_coords[1], *z_coords[1]]
    coords[2] = [*x_coords[2], *y_coords[2], *z_coords[2]]

    voxel = []
    for i in range(0, coords[0].size * coords[1].size * coords[2].size):
        voxel.append([])

    # поиск координат вокселя для каждой точки
    voxel_x = np.searchsorted(coords[0], arr[0])
    voxel_y = np.searchsorted(coords[1], arr[1])
    voxel_z = np.searchsorted(coords[2], arr[2])

    # заполнение вокселей точками
    for point in range(len(arr[0])):
        voxel[voxel_x[point] * coords[0].size + voxel_y[point] * coords[1].size + voxel_z[point] * coords[
            2].size].append([arr[0][point], arr[1][point], arr[2][point]])

    # прореживание вокселей
    for i in range(len(voxel)):
        if len(voxel[i]) > rand_param:
            for j in range(rand_param):
                voxel[i].remove(voxel[i][random.randint(0, len(voxel[i]) - 1)])

    arr_filtered = []

    filled_voxel = list(filter(None, voxel))
    for i in range(len(filled_voxel)):
        for j in range(len(filled_voxel[i])):
            arr_filtered.append(filled_voxel[i][j])

    cloud_filtered = pcl.PointCloud()
    cloud_filtered.from_array(np.array(arr_filtered).astype(np.float32))

    pcl.save(cloud_filtered, 'data/lamppost_rand.pcd')

    print("initial size ", cloud.size)
    print("optimized size ", cloud_filtered.size)


if __name__ == "__main__":
    main()
