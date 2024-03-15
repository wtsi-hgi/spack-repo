# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransformr(RPackage):
	"""Polygon and Path Transformations

	In order to smoothly animate the transformation of polygons and 
    paths, many aspects needs to be taken into account, such as differing number 
    of control points, changing center of rotation, etc. The 'transformr' 
    package provides an extensive framework for manipulating the shapes of 
    polygons and paths and can be seen as the spatial brother to the 'tweenr' 
    package.
	"""
	
	homepage = "https://github.com/thomasp85/transformr"
	cran = "transformr" 

	version("0.1.5", md5="c874d7ab2e7c979c43c89fa6dcbb1f87")

	depends_on("r-tweenr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
