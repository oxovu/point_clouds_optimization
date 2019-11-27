import numpy as np
import pcl
import random


def main():
    cloud = pcl.load('data/lamppost.pcd')

    # удаление точек с большим колличеством соседей
    sor = cloud.make_statistical_outlier_filter()
    # колличество соседей
    sor.set_mean_k(1)
    # радиус поиска соседей
    sor.set_std_dev_mul_thresh(0.1)
    sor.set_negative(True)
    cloud_filtered = sor.filter()

    pcl.save(cloud_filtered, 'data/lamppost3.pcd')

    print("initial size ", cloud.size)
    print("optimized size ", cloud_filtered.size)


if __name__ == "__main__":
    main()
