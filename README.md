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

#### Code Structure for Fab+LLM Proj
``` bash
RANSAC-3D
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
```


#### Note for Fab+LLM Proj
Search for the 'potential frontend' in the code to see where to add the frontend code POTENTIALLY.


#### Features:
 - [Plane](https://leomariga.github.io/pyRANSAC-3D/api-documentation/plane/)
 - [Cylinder](https://leomariga.github.io/pyRANSAC-3D/api-documentation/cylinder/)
 - [Cuboid](https://leomariga.github.io/pyRANSAC-3D/api-documentation/cuboid/)
 - [Sphere](https://leomariga.github.io/pyRANSAC-3D/api-documentation/sphere/)
 - [Line](https://leomariga.github.io/pyRANSAC-3D/api-documentation/line/)
 - [Circle](https://leomariga.github.io/pyRANSAC-3D/api-documentation/circle/)
 - [Point](https://leomariga.github.io/pyRANSAC-3D/api-documentation/point/)




## Take a look: 

### Example 1 - Planar RANSAC

``` python
import pyransac3d as pyrsc

points = load_points(.) # Load your point cloud as a numpy array (N, 3)

plane1 = pyrsc.Plane()
best_eq, best_inliers = plane1.fit(points, 0.01)

```

Results in the plane equation Ax+By+Cz+D:
`[0.720, -0.253, 0.646, 1.100]`

### Example 2 - Spherical RANSAC

Loading a noisy sphere's point cloud with r = 5 centered in 0 we can use the following code:

``` python
import pyransac3d as pyrsc

points = load_points(.) # Load your point cloud as a numpy array (N, 3)

sph = pyrsc.Sphere()
center, radius, inliers = sph.fit(points, thresh=0.4)

```

Results:
``` python
center: [0.010462385575072288, -0.2855090643954039, 0.02867848979091283]
radius: 5.085218633039647
```

![3D Sphere](https://raw.githubusercontent.com/leomariga/pyRANSAC-3D/master/doc/sphere.gif "3D Sphere")


## Documentation & other links
 - The [documentation is this Ṕage](https://leomariga.github.io/pyRANSAC-3D/).
 - Source code in the [Github repository](https://github.com/leomariga/pyRANSAC-3D).
 - [Pypi pakage installer](https://pypi.org/project/pyransac3d/)
 - You can find the animations you see in the documentation on branch [Animations](https://github.com/leomariga/pyRANSAC-3D/tree/Animations). It needs [Open3D](https://github.com/intel-isl/Open3D) library to run. The Animation branch is not regularly maintained, it only exists to create some cool visualizations ;D 


## License
[Apache 2.0](https://github.com/leomariga/pyRANSAC-3D/blob/master/LICENSE)

## Citation
Did this repository was useful for your work? =)

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

## Contributing is awesome!

See [CONTRIBUTING](https://github.com/leomariga/pyRANSAC-3D/blob/master/CONTRIBUTING.md)




## Contact


