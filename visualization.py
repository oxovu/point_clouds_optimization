import pcl
import pcl.pcl_visualization


def main():
    viewer = pcl.pcl_visualization.PCLVisualizering()

    cloud = pcl.load('data/lamppost.pcd')

    while 1:
        # Visualizing pointcloud
        viewer.AddPointCloud(cloud, b'scene_cloud', 0)
        viewer.SpinOnce()
        viewer.RemovePointCloud(b'scene_cloud', 0)


if __name__ == "__main__":
    main()
