# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoxr(RPackage):
	"""Trees Geometry and Morphology from Unstructured TLS Data

	Tools for 3D point cloud voxelisation, projection, geometrical and morphological description of trees (DBH, height, volume, crown diameter), analyses of temporal changes between different measurement times, distance based clustering and visualisation of 3D voxel clouds and 2D projection. Most analyses and algorithms provided in the package are based on the concept of space exploration and are described in Lecigne et al. (2018, <doi:10.1093/aob/mcx095>).
	"""
	
	homepage = "https://github.com/Blecigne/VoxR"
	cran = "VoxR" 

	version("1.0.0", md5="ef1f1216db2d61a8fcc37f1e725fea36")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
