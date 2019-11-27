from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
import pcl
from mpl_toolkits.mplot3d import Axes3D
from plotXYZ import plot_bounds


def main():
    # оптимизированное облако
    cloud1 = pcl.load('data/lamppost2.pcd')
    # начальное облако
    cloud2 = pcl.load('data/lamppost.pcd')

    points1 = cloud1.to_array()
    points2 = cloud2.to_array()

    # построение триангуляции
    tri = Delaunay(points1)

    x = []
    y = []
    z = []

    for point in points1:
        x.append(float(point[0]))
        y.append(float(point[1]))
        z.append(float(point[2]))

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    # граффическое изображение
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1, projection='3d')
    #
    # plot_bounds(ax, x, y, z)
    #
    # ax.plot_trisurf(x, y, z, triangles=tri.simplices)
    # plt.show()

    error = 0.0
    i = 0

    # подсчет общей ошибки
    for point in points2:
        i += 1
        dist = tri.plane_distance(point)
        min_dist = min(abs(dist))
        print("step ", i, "\terror ", min_dist)
        error += min_dist
    print("\nerror sum ", error)
    print("\nerror sum/points number ", error/points1.size)


if __name__ == "__main__":
    main()
