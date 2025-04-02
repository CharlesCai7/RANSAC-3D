#### Getting Start for Fab+LLM Proj
``` bash
python -m venv ransacEnv
source ransacEnv/bin/activate
```

``` bash
pip install -r requirements-dev.txt
pip install -r requirements.txt
python setup.py develop
```

``` bash
python ply2shape.py
```

#### Code Structure for Fab+LLM Proj
``` bash
RANSAC-3D
├── setup.py (setup the python package)
├── assets
│   ├── mesh_models
│   ├── models_ply
├── pyransac3d
│   ├── __init__.py
│   ├── plane.py
│   ├── cylinder.py
│   ├── cuboid.py
│   ├── sphere.py
│   ├── line.py
│   ├── circle.py
├── tests (example testing code)
├── config.py (define mesh based model to process and the RANSAC parameters)
├── mesh2ply.py & ply2shape.py (mesh models -> pointcloud files -> shape info returned)
├── recoder.py (reverse engineering the mesh models into cadquery code with recoder)
├── iou.py (intersection over union, to calculate the accuracy of the resulted model by recoder)
├── main.py (run the recoder.py first, then determine if we should use the model directly with IoU)
```


#### Note for Fab+LLM Proj
Search for the 'potential frontend' in the code to see where to add the frontend code POTENTIALLY.


#### Features:
 - [Plane](https://leomariga.github.io/pyRANSAC-3D/api-documentation/plane/)
 - [Cylinder (rebuilt)](https://leomariga.github.io/pyRANSAC-3D/api-documentation/cylinder/)
 - [Cuboid](https://leomariga.github.io/pyRANSAC-3D/api-documentation/cuboid/)
 - [Sphere](https://leomariga.github.io/pyRANSAC-3D/api-documentation/sphere/)
 - [Line](https://leomariga.github.io/pyRANSAC-3D/api-documentation/line/)
 - [Circle](https://leomariga.github.io/pyRANSAC-3D/api-documentation/circle/)
 - [Point](https://leomariga.github.io/pyRANSAC-3D/api-documentation/point/)


## Citation

1. pyRANSAC package (update the cylinder model):
```
@software{Mariga_pyRANSAC-3D_2022,
  author = {Mariga, Leonardo},
  doi = {10.5281/zenodo.7212567},
  month = {10},
  title = {{pyRANSAC-3D}},
  url = {https://github.com/leomariga/pyRANSAC-3D},
  version = {v0.6.0},
  year = {2022}
}
```
2. CAD-Recode: Reverse Engineering CAD Code from Point Clouds
```
@misc{rukhovich2025cadrecodereverseengineeringcad,
      title={CAD-Recode: Reverse Engineering CAD Code from Point Clouds}, 
      author={Danila Rukhovich and Elona Dupont and Dimitrios Mallis and Kseniya Cherenkova and Anis Kacem and Djamila Aouada},
      year={2025},
      eprint={2412.14042},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2412.14042}, 
}
```

