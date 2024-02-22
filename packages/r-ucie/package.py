# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcie(RPackage):
	"""Mapping 3D Data into CIELab Color Space

	Returns a data frame with the names of the input data points and hex colors (or CIELab coordinates). Data can be mapped to colors for use in data visualization. It optimally maps data points into a polygon that represents the CIELab colour space. Since Euclidean distance approximates relative perceptual differences in CIELab color space, the result is a color encoding that aims to capture much of the structure of the original data. 
	"""
	
	cran = "ucie" 

	version("1.0.2", md5="6f6810f5a5462476987ba90059aa2d1f")

	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ptinpoly", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
