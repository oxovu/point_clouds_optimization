import pcl


def main():
    cloud = pcl.load('data/lamppost.pcd')

    # аппроксимация внутри каждого вокселя
    voxel = cloud.make_voxel_grid_filter()
    # размеры вокселя
    voxel.set_leaf_size(0.045, 0.045, 0.045)
    cloud_filtered = voxel.filter()

    pcl.save(cloud_filtered, 'data/lamppost2.pcd')

    print("initial size ", cloud.size)
    print("optimized size ", cloud_filtered.size)


if __name__ == "__main__":
    main()
