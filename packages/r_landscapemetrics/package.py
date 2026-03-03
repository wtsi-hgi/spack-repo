# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandscapemetrics(RPackage):
	"""Landscape Metrics for Categorical Map Patterns

	Calculates landscape metrics for categorical landscape patterns in 
    a tidy workflow. 'landscapemetrics' reimplements the most common metrics from
    'FRAGSTATS' (<https://www.fragstats.org/>) and new ones from the current 
    literature on landscape metrics. This package supports 'terra' SpatRaster objects 
    as input arguments. It further provides utility functions to visualize patches, 
    select metrics and building blocks to develop new metrics.
	"""
	
	homepage = "https://r-spatialecology.github.io/landscapemetrics/"
	cran = "landscapemetrics" 

	version("2.1.1", md5="2de31dda3f3ca17e5e47897d7afcf3d6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
