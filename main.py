import optimizations
import comparison
import pcl
from time import time


def main():
    cloud = pcl.load('data/milk.pcd')
    cloud1 = pcl.load('data/milk.pcd')
    cloud2 = pcl.load('data/milk.pcd')

    # print('org')
    # print('dist = ', comparison.c2c_distance(cloud, cloud))
    # print('size = ', comparison.c2c_size(cloud, cloud))

    start = time()
    voxel_cloud = optimizations.voxel(cloud, 0.0031, 0.0031, 0.0031)
    end = time()
    print('voxel')
    print('time = ', end - start)
    print('dist = ', comparison.c2c_distance(voxel_cloud, cloud))
    print('size = ', comparison.c2c_size(cloud, voxel_cloud))

    start = time()
    sor_cloud = optimizations.sor(cloud1, 7, 0.00001)
    end = time()
    print('sor')
    print('time = ', end - start)
    print('dist = ', comparison.c2c_distance(sor_cloud, cloud))
    print('size = ', comparison.c2c_size(cloud, sor_cloud))

    start = time()
    rand_cloud = optimizations.rand(cloud2, 2, 7200)
    end = time()
    print('rand')
    print('time = ', end - start)
    print('dist = ', comparison.c2c_distance(rand_cloud, cloud))
    print('size = ', comparison.c2c_size(cloud, rand_cloud))


"""
             result example
voxel
time =  0.0008120536804199219
dist =  2.7635448593573273e-07
size =  0.4269582504970179
sor
time =  0.021006107330322266
dist =  5.078507019032886e-07
size =  0.4279920477137177
rand
time =  1.0679066181182861
dist =  2.391338733629257e-07
size =  0.4274353876739563

"""

if __name__ == "__main__":
    main()
