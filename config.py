# config.py - Store shared settings for all scripts
# File name
FILE_NAME = "stlhardwareparts_planetaryspinner"
# STL file name

# IoU threshold for comparison
IOU_THRESHOLD = 0.7
# Path to the STL file
TEST_FILE = "assets/mesh_models/" + FILE_NAME + ".stl"
# Where to save the generated point cloud  
OUTPUT_POINTCLOUD = "assets/models_ply/" + FILE_NAME + ".ply"
# Where to save the generated point cloud CSV
OUTPUT_POINTCLOUD_CSV = "assets/models_ply/" + FILE_NAME + ".csv"
# Number of points to sample from the mesh
NUMBER_OF_POINTS = 10000
# RANSAC parameters
RANSAC_N = 3
RANSAC_ITERATIONS = 1000