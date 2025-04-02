import config
import iou
import recoder
import mesh2ply
import ply2shape


def main():
    recoder.recode()
    IoU = iou.calculate_iou()
    if IoU < config.IoU_THRESHOLD:
        print("IoU is below the threshold. Ready to proceed with LLM...")
    else:
        print("IoU is above the threshold. Generating geometry info instead ...")
        mesh2ply.generate_pointcloud()
        ply2shape.convert_ply_to_shape() 