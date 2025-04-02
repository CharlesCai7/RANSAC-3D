import os
import shutil
import config
from gradio_client import Client, handle_file

# Initialize the client
client = Client("filapro/cad-recode")


def recode():
    # Call the point cloud API endpoint with file input and seed
    point_cloud_result = client.predict(
        in_mesh_path=handle_file(config.TEST_FILE),
        seed=42,
        api_name="/run_point_cloud"
    )
    point_cloud_path = "assets/recoder_obj/" + f"_{config.FILE_NAME}.obj"
    shutil.move(point_cloud_result, point_cloud_path)
    print("Point Cloud Result saved to:", point_cloud_path)

    # Call the CAD recode API endpoint
    cad_recode_result = client.predict(api_name="/run_cad_recode")
    print("CAD Recode Result:", cad_recode_result)

    # Call the mesh API endpoint
    mesh_result = client.predict(api_name="/run_mesh")
    mesh_path = "assets/recoder_mesh/" + f"_{config.FILE_NAME}_param.stl"
    shutil.move(mesh_result, mesh_path)
    print("Mesh Result saved to:", mesh_path)


