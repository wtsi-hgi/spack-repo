# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHabtools(RPackage):
	"""Tools and Metrics for 3D Surfaces and Objects

	
    A collection of functions for sampling and simulating 3D surfaces and objects 
    and estimating metrics like rugosity, fractal dimension, convexity, sphericity, circularity, 
    second moments of area and volume, and more.   
	"""
	
	homepage = "https://jmadinlab.github.io/habtools/"
	cran = "habtools" 

	version("1.0.5", md5="9fa4eb17d455ac19103465579a8792df")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-raster@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
