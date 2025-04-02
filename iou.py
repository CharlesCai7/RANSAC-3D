# calculate the IoU of two point clouds
import open3d as o3d
import numpy as np
import config
import mesh2ply
import pyransac3d as pyrsc


def calculate_iou(pcd1, pcd2):
    """
    Calculate the Intersection over Union (IoU) of two point clouds.
    :param pcd1: First point cloud
    :param pcd2: Second point cloud
    :return: IoU value
    """
    # Convert point clouds to numpy arrays
    points1 = np.asarray(pcd1.points)
    points2 = np.asarray(pcd2.points)
    # Create a set of points for each point cloud
    set1 = set(map(tuple, points1))
    set2 = set(map(tuple, points2))
    # Calculate the intersection and union
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    # Calculate IoU
    iou = len(intersection) / len(union) if len(union) > 0 else 0
    return iou