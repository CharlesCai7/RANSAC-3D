import open3d as o3d
import numpy as np
import config
import pandas as pd

def generate_pointcloud():
    print(f"Using test file: {config.TEST_FILE}")

    mesh = o3d.io.read_triangle_mesh(config.TEST_FILE)
    pcd = mesh.sample_points_poisson_disk(number_of_points=config.NUMBER_OF_POINTS)
    pcd.paint_uniform_color([0.7, 0.7, 0.7])
    o3d.io.write_point_cloud(config.OUTPUT_POINTCLOUD, pcd)

    # (potential frontend) visualization
    # o3d.visualization.draw_geometries([pcd])

    print(f"Point cloud saved to {config.OUTPUT_POINTCLOUD}")

def generate_pointcloud_csv():
    # Load the point cloud from the ply file
    print(f"Using test file: {config.OUTPUT_POINTCLOUD}")
    # read the point cloud
    pcd = o3d.io.read_point_cloud(config.OUTPUT_POINTCLOUD)
    # Convert to numpy array
    points = np.asarray(pcd.points)
    # Save to CSV
    df = pd.DataFrame(points, columns=['x', 'y', 'z'])
    df.to_csv(config.OUTPUT_POINTCLOUD_CSV, index=False)
    print(f"Point cloud CSV saved to {config.OUTPUT_POINTCLOUD_CSV}")

if __name__ == "__main__":
    generate_pointcloud()
    generate_pointcloud_csv()
