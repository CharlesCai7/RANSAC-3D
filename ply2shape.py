import numpy as np
import open3d as o3d
import pyransac3d as pyrsc
import matplotlib.pyplot as plt
import config
import mesh2ply
import copy


def process_pointcloud():
    # Ensure the point cloud is generated
    mesh2ply.generate_pointcloud()

    print(f"Loading point cloud from: {config.OUTPUT_POINTCLOUD}")

    try:
        # Load the point cloud
        pcd = o3d.io.read_point_cloud(config.OUTPUT_POINTCLOUD)
        print(f"Loaded point cloud with {len(pcd.points)} points")

        # (potential frontend) Visualize the point cloud
        # o3d.visualization.draw_geometries([pcd])

    except Exception as e:
        print("Error loading point cloud:", e)

    return pcd


def dbscan_clustering(pcd):
    # Convert the point cloud to a numpy array
    points = np.asarray(pcd.points)
    # DBSCAN clustering
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        labels = np.array(pcd.cluster_dbscan(eps=0.05, min_points=5, print_progress=True))
    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")
    colors = plt.get_cmap("tab10")(labels / (max_label if max_label > 0 else 1))
    colors[labels < 0] = 0
    pcd.colors = o3d.utility.Vector3dVector(colors[:, :3])
    o3d.visualization.draw_geometries([pcd])


def detect_circle(pcd):
    max_circle_num = 1
    segment_models = {}
    segments = {}

    points = np.asarray(pcd.points)

    for i in range(max_circle_num):
        cir = pyrsc.Circle()
        center = [0, 0, 0]
        radius = 0
        normal = [0, 0, 0]
        inliers = []
        while radius < 0.1 or radius > 100:
            center, normal, radius, inliers = cir.fit(points, thresh=0.5)

        print(f"\n This model has a circle based primitive, with the center at " + str(center) +
              ", radius " + str(radius) + " and normal vector " + str(normal) + "\n")
        
        # handle division by zero, adding an offset to the normal vector
        if normal[2] == 0: normal[2] = 0.001
        
        R = pyrsc.get_rotationMatrix_from_vectors([0, 0, 1], normal)

        inline = pcd.select_by_index(inliers).paint_uniform_color([1, 0, 0])

        mesh_circle = o3d.geometry.TriangleMesh.create_torus(torus_radius=radius, tube_radius=1)
        mesh_circle.compute_vertex_normals()
        mesh_circle.paint_uniform_color([0.9, 0.1, 0.1])
        mesh_circle = mesh_circle.rotate(R, center=[0, 0, 0])
        mesh_circle = mesh_circle.translate((center[0], center[1], center[2]))

        segments[i] = mesh_circle
   
    segments[max_circle_num] = pcd
    o3d.visualization.draw_geometries(list(segments.values()))

def detect_plane(pcd):
    max_plane_num = 6
    segment_models = {}
    segments = {}
    rest = pcd
    for i in range(max_plane_num):
        colors = plt.get_cmap("tab20")(i)
        plane_model, inliers = rest.segment_plane(distance_threshold=config.RANSAC_THRESHOLD, ransac_n=config.RANSAC_N,
                                                  num_iterations=config.RANSAC_ITERATIONS)
        if len(inliers) < 200:
            break
        segment_models[i] = plane_model
        segments[i] = rest.select_by_index(inliers)
        segments[i].paint_uniform_color(colors[:3])
        rest = rest.select_by_index(inliers, invert=True)
        print(f"Plane {i} equation: {plane_model}")
    o3d.visualization.draw_geometries(list(segments.values()))


def detect_cylinder(pcd):
    # Convert the point cloud to a numpy array
    points = np.asarray(pcd.points)
    cil = pyrsc.Cylinder()
    center, normal, radius, inliers = cil.fit(points, thresh=0.05)
    print("center: " + str(center))
    print("radius: " + str(radius))
    print("vecC: " + str(normal))
    R = pyrsc.get_rotationMatrix_from_vectors([0, 0, 1], normal)

    plane = pcd.select_by_index(inliers).paint_uniform_color([1, 0, 0])
    not_plane = pcd.select_by_index(inliers, invert=True)
    mesh = o3d.geometry.TriangleMesh.create_coordinate_frame(origin=[0, 0, 0], size=0.2)
    cen = o3d.geometry.TriangleMesh.create_coordinate_frame(origin=center, size=0.5)
    mesh_rot = copy.deepcopy(mesh).rotate(R, center=[0, 0, 0])

    mesh_cylinder = o3d.geometry.TriangleMesh.create_cylinder(radius=radius, height=0.5)
    mesh_cylinder.compute_vertex_normals()
    mesh_cylinder.paint_uniform_color([0.1, 0.9, 0.1])
    mesh_cylinder = mesh_cylinder.rotate(R, center=[0, 0, 0])
    mesh_cylinder = mesh_cylinder.translate((center[0], center[1], center[2]))
    o3d.visualization.draw_geometries([mesh_cylinder])

    o3d.visualization.draw_geometries([plane, not_plane, mesh, mesh_rot, mesh_cylinder])

    # remove the points that are not part of the cylinder
    pcd = pcd.select_by_index(inliers)
    o3d.visualization.draw_geometries([pcd])

def detect_primitives():
    pcd = process_pointcloud()
    detect_circle(pcd)
    # detect_plane(pcd)
    # detect_cylinder(pcd)



if __name__ == "__main__":
    detect_primitives()
