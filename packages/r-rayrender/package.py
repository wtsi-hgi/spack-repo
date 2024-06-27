# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRayrender(RPackage):
    """Build and Raytrace 3D Scenes

    Render scenes using pathtracing. Build 3D scenes out of spheres, cubes, planes, disks, triangles, cones, curves, line segments, cylinders, ellipsoids, and 3D models in the 'Wavefront' OBJ file format or the PLY Polygon File Format. Supports several material types, textures, multicore rendering, and tone-mapping. Based on the "Ray Tracing in One Weekend" book series. Peter Shirley (2018) <https://raytracing.github.io>.
    """

    homepage = "https://www.rayrender.net"
    cran = "rayrender"

    version("0.32.2", md5="5513c674f93c1b8e70568b190f0c7271")

    depends_on("r@3.0.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-raster", type=("build", "run"))
    depends_on("r-decido", type=("build", "run"))
    depends_on("r-rayimage@0.10:", type=("build", "run"))
    depends_on("r-progress", type=("build", "run"))
    depends_on("r-rayvertex@0.10.4:", type=("build", "run"))
    depends_on("r-withr", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-pillar", type=("build", "run"))
    depends_on("r-rcppthread", type=("build", "run"))
    depends_on("r-spacefillr@0.3:", type=("build", "run"))

    @run_before("install")
    def set_ac_unique_file(self):
        touch("rayrender")
