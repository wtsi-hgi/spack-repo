# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmarchingcubes(RPackage):
	"""Calculate 3D Contour Meshes Using the Marching Cubes Algorithm

	A port of the C++ routine for applying the marching cubes algorithm written by 
    Thomas Lewiner et al. (2012) <doi:10.1080/10867651.2003.10487582> into an R package. 
    The package supplies the contour3d() function, which takes a 3-dimensional array of voxel 
    data and calculates the vertices, vertex normals, and faces for a 3d mesh representing 
    the contour(s) at a given level.
	"""
	
	homepage = "https://github.com/shwilks/rmarchingcubes"
	cran = "rmarchingcubes" 

	version("0.1.3", md5="5063ae53588ef894864b8524cfd2e475")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
