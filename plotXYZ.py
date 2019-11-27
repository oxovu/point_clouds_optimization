import pcl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def main():
    cloud = pcl.load('data/lamppost.pcd')

    shape = cloud.to_array().transpose()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    x = shape[0]
    y = shape[1]
    z = shape[2]

    ax.scatter(x, y, z)

    plt.show()


def plot_bounds(ax, x, y, z):
    max_dist = np.array([x.max() - x.min(), y.max() - y.min(), z.max() - z.min()]).max() / 2.0

    mean_x = (x.max() + x.min()) / 2
    mean_y = (y.max() + y.min()) / 2
    mean_z = (z.max() + z.min()) / 2
    ax.set_xlim(mean_x - max_dist, mean_x + max_dist)
    ax.set_ylim(mean_y - max_dist, mean_y + max_dist)
    ax.set_zlim(mean_z - max_dist, mean_z + max_dist)


if __name__ == "__main__":
    main()
