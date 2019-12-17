from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
import pcl


def c2c_distance(cloud1, cloud2):
    points1 = cloud1.to_array()
    points2 = cloud2.to_array()

    # построение триангуляции
    tri = Delaunay(points1)

    distance = 0.0
    i = 0

    # подсчет общего расстояния
    for point in points2:
        i += 1
        dist = tri.plane_distance(point)
        min_dist = min(abs(dist))
        distance += min_dist

    return distance/cloud1.size


def c2c_size(cloud1, cloud2):
    return cloud2.size / cloud1.size
