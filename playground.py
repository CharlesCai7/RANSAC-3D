import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import numpy as np
from scipy.optimize import minimize, basinhopping, brute
from sklearn.decomposition import PCA
import config


PATH_TO_POINT_CLOUD = config.OUTPUT_POINTCLOUD_CSV
# header is x,y,z, so skip the first line
points = pd.read_csv(PATH_TO_POINT_CLOUD, skiprows=1, header=None)

points.columns = ['x', 'y', 'z']


def proj(x, y):
    if x.shape == y.shape:
        # single x vector
        return y * (np.dot(x, y) / np.dot(y, y))
    else:
        # broadcast along x
        return y[np.newaxis, :] * (np.dot(x, y) / np.dot(y, y))[:, np.newaxis]


def scalar_proj(x, y):
    if x.shape == y.shape:
        # single x vector
        return (np.dot(x, y) / np.dot(y, y))
    else:
        # broadcast along x
        return (np.dot(x, y) / np.dot(y, y))[:, np.newaxis]
    
    
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
        raise Exception("Division by zero in normalize")
    return v / norm


def distance_from_central_axis(cyl_center, cyl_vec, point_vec):
    cyl_vec = normalize(cyl_vec)
    point_offset = point_vec - cyl_center
    center_to_point = point_offset - proj(point_offset, cyl_vec)
    distance = np.linalg.norm(center_to_point, axis=1)
    return distance


def distance_along_central_axis(cyl_center, cyl_vec, point_vec):
    cyl_vec = normalize(cyl_vec)
    point_offset = point_vec - cyl_center
    signed_distance_along_central_axis = scalar_proj(point_offset, cyl_vec)
    return signed_distance_along_central_axis


def cylinder_radius(cyl_center, cyl_vec, point_vec):
    return np.mean(distance_from_central_axis(cyl_center, cyl_vec, point_vec))


def cylinder_height(cyl_center, cyl_vec, point_vec):
    distance = distance_along_central_axis(cyl_center, cyl_vec, point_vec)
    return np.min(distance), np.max(distance)


def cost_func(x, points):
    a, b, c, d, e, f = x
    cyl_center = np.array([a, b, c])
    cyl_vec = np.array([d, e, f])
    distances = distance_from_central_axis(cyl_center, cyl_vec, points)
    # Minimize variance of distance
    cost = np.std(distances)
    # Also penalize having center off-center
    off_center_penalty = distance_along_central_axis(cyl_center, cyl_vec, points).mean()
    cost += off_center_penalty ** 2
    return cost


def guess_cyl_vec(points):
    return PCA(n_components=1).fit(points).components_[0]


def find_cyl_center_and_vec(points, n_iter=10):
    points_npy = points.values
    
    # Note: this fit is running in a loop because I found that the minimizer
    # got trapped in local minima if provided with a bad initial guess.
    # To compensate for this, run the fit 10 times and pick the best one.
    best = None
    for i in range(n_iter):
        x0 = np.random.normal(scale=1e-3, size=6)
        # Use mean as position guess instead of random
        x0[0:3] = points_npy.mean(axis=0)
        options = {
            'eps': 1e-9
        }
        res = minimize(lambda x: cost_func(x, points_npy), x0=x0, options=options, method='BFGS')
        if best is None or res.fun < best.fun:
            best = res
    cyl_center, cyl_vec = best.x.reshape([2, 3])
    cyl_vec = normalize(cyl_vec)
    # Force Z to be non-negative
    if cyl_vec[2] < 0:
        cyl_vec = -cyl_vec
    return cyl_center, cyl_vec


def get_cylinder_points(cyl_center, cyl_vec, radius, height_min, height_max):
    t_height = np.linspace(height_min, height_max, 1000)[:, np.newaxis]
    turns = 10
    t_rot = np.linspace(0, 2*turns*np.pi, 1000)[:, np.newaxis]
    central_axis = cyl_center + t_height * cyl_vec[np.newaxis]
    # Get orthoganal vectors using Gramm-Schmitt
    rotvec1 = np.random.randn(3)
    rotvec1 -= rotvec1.dot(cyl_vec) * cyl_vec
    rotvec1 /= np.linalg.norm(rotvec1)
    rotvec2 = np.cross(cyl_vec, rotvec1)
    cylinder_points = central_axis.copy()
    cylinder_points += radius * np.cos(t_rot) * rotvec1[np.newaxis]
    cylinder_points += radius * np.sin(t_rot) * rotvec2[np.newaxis]
    return cylinder_points


def main():
    cyl_center, cyl_vec = find_cyl_center_and_vec(points)
    radius = cylinder_radius(cyl_center, cyl_vec, points.values)
    height_min, height_max = cylinder_height(cyl_center, cyl_vec, points.values)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(*points.values.T)
    ax.scatter(*get_cylinder_points(cyl_center, cyl_vec, radius, height_min, height_max).T)
    print (f"Center: {cyl_center}, Vec: {cyl_vec}, Radius: {radius}, Height: {height_min} to {height_max}")
    plt.show()