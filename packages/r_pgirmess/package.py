# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgirmess(RPackage):
	"""Spatial Analysis and Data Mining for Field Ecologists

	Set of tools for reading, writing and transforming spatial and seasonal data, model selection and specific statistical tests for ecologists. It includes functions to interpolate regular positions of points between landmarks, to discretize polylines into regular point positions, link distant observations to points and convert a bounding box in a spatial object. It also provides miscellaneous functions for field ecologists such as spatial statistics and inference on diversity indexes, writing data.frame with Chinese characters.
	"""
	
	homepage = "https://github.com/pgiraudoux/pgirmess"
	cran = "pgirmess" 

	version("2.0.3", md5="3db3f12d9774800a6dc9243f8bf0ed8e")

	depends_on("r-boot@1.3.4:", type=("build", "run"))
	depends_on("r-sf@1.0.4:", type=("build", "run"))
	depends_on("r-sp@0.9.97:", type=("build", "run"))
	depends_on("r-spdep@1.1.7:", type=("build", "run"))
