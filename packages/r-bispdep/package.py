# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBispdep(RPackage):
	"""Statistical Tools for Bivariate Spatial Dependence Analysis

	A collection of functions to test spatial autocorrelation between variables, including Moran I, Geary C and Getis G together with scatter plots, functions for mapping and identifying clusters and outliers, functions associated with the moments of the previous statistics that will allow testing whether there is bivariate spatial autocorrelation, and a function that allows identifying (visualizing neighbours) on the map, the neighbors of any region once the scheme of the spatial weights matrix has been established.
	"""
	
	cran = "bispdep" 

	version("1.0-0", md5="53532c214c5022c73c28985cbe905e10")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-boot@1.3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp@1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
