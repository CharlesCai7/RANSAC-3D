# config.py - Store shared settings for all scripts

# Path to the STL file
TEST_FILE = "assets/mesh_models/coffee_mug.stl"
# Where to save the generated point cloud  
OUTPUT_POINTCLOUD = "assets/models_ply/coffee_mug.ply"  
# Number of points to sample from the mesh
NUMBER_OF_POINTS = 10000
# RANSAC parameters
RANSAC_THRESHOLD = 0.01  
RANSAC_N = 3
RANSAC_ITERATIONS = 1000