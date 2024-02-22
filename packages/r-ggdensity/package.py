# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdensity(RPackage):
	"""Interpretable Bivariate Density Visualization with 'ggplot2'

	The 'ggplot2' package provides simple functions for visualizing contours
  of 2-d kernel density estimates. 'ggdensity' implements several additional density estimators 
  as well as more interpretable visualizations based on highest density regions instead of
  the traditional height of the estimated density surface. 
	"""
	
	homepage = "https://jamesotto852.github.io/ggdensity/"
	cran = "ggdensity" 

	version("1.0.0", md5="4ed086a32848a5125b3dd981689d4492")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
