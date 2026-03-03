# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuadmesh(RPackage):
	"""Quadrangle Mesh

	Create surface forms from matrix or 'raster' data for flexible plotting and
 conversion to other mesh types. The functions 'quadmesh' or 'triangmesh'
 produce a continuous surface as a 'mesh3d' object as used by the 'rgl'
 package. This is used for plotting raster data in 3D (optionally with
 texture), and allows the application of a map projection without data loss and 
 many processing applications that are restricted by inflexible regular grid rasters.
 There are discrete forms of these continuous surfaces available with
 'dquadmesh' and 'dtriangmesh' functions.
	"""
	
	homepage = "https://github.com/hypertidy/quadmesh"
	cran = "quadmesh" 

	version("0.5.5", md5="3aa02216c3f02bfac66399d54ccfe909")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-reproj@0.4:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-palr", type=("build", "run"))
