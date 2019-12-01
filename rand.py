import pcl
import pcl.pcl_visualization
import numpy as np


def main():
    step = 10

    viewer = pcl.pcl_visualization.PCLVisualizering()
    cloud = pcl.load('data/stanford_bunny/data/bun090_UnStructured.pcd')

    arr = cloud.to_array().transpose()

    xyzmin = arr.min(0)
    xyzmax = arr.max(0)

    xmin = arr[0].min()
    xmax = arr[0].max()

    ymin = arr[1].min()
    ymax = arr[1].max()

    zmin = arr[2].min()
    zmax = arr[2].max()

    x_y_z = [arr[0], arr[1], arr[2]]

    segments = []
    s = np.linspace(xmin, xmax, step)
    segments.append(s)
    s = np.linspace(ymin, ymin, step)
    segments.append(s)
    s = np.linspace(zmin, zmin, step)
    segments.append(s)

    segments1 = []
    s = np.linspace(xmin, xmin, step)
    segments1.append(s)
    s = np.linspace(ymin, ymax, step)
    segments1.append(s)
    s = np.linspace(zmin, zmin, step)
    segments1.append(s)

    segments2 = []
    s = np.linspace(xmin, xmin, step)
    segments2.append(s)
    s = np.linspace(ymin, ymin, step)
    segments2.append(s)
    s = np.linspace(zmin, zmax, step)
    segments2.append(s)

    full_seg = np.empty([3, step * 3])

    full_seg[0] = [*segments[0], *segments1[0], *segments2[0]]
    full_seg[1] = [*segments[1], *segments1[1], *segments2[1]]
    full_seg[2] = [*segments[2], *segments1[2], *segments2[2]]

    new_cloud_arr = np.array(full_seg).astype(np.float32).transpose()
    new_cloud = pcl.PointCloud()
    new_cloud.from_array(new_cloud_arr)

    while 1:
        # Visualizing pointcloud
        viewer.AddPointCloud(new_cloud, b'scene_cloud', 0)
        viewer.AddPointCloud(cloud, b'scene_cloud1', 0)
        viewer.SpinOnce()
        viewer.RemovePointCloud(b'scene_cloud', 0)
        viewer.RemovePointCloud(b'scene_cloud1', 0)


if __name__ == "__main__":
    main()
