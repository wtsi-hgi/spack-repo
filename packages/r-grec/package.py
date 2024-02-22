# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrec(RPackage):
	"""Gradient-Based Recognition of Spatial Patterns in Environmental
Data

	Provides algorithms for detection of spatial patterns from oceanographic data using image processing methods based on Gradient Recognition.
	"""
	
	homepage = "https://github.com/LuisLauM/grec"
	cran = "grec" 

	version("1.6.0", md5="98bf61dd835bf410220215aced212507")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-imagine@2.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
