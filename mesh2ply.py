import open3d as o3d
import numpy as np
import config

def generate_pointcloud():
    print(f"Using test file: {config.TEST_FILE}")

    mesh = o3d.io.read_triangle_mesh(config.TEST_FILE)
    pcd = mesh.sample_points_poisson_disk(number_of_points=config.NUMBER_OF_POINTS)
    pcd.paint_uniform_color([0.7, 0.7, 0.7])
    o3d.io.write_point_cloud(config.OUTPUT_POINTCLOUD, pcd)

    # o3d.visualization.draw_geometries([pcd])

    print(f"Point cloud saved to {config.OUTPUT_POINTCLOUD}")

if __name__ == "__main__":
    generate_pointcloud()
