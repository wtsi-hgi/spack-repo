# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDensityarea(RPackage):
	"""Polygons of Bivariate Density Distributions

	With bivariate data, it is possible to calculate
    2-dimensional kernel density estimates that return polygons at given
    levels of probability. 'densityarea' returns these polygons for
    analysis, including for calculating their area.
	"""
	
	homepage = "https://github.com/JoFrhwld/densityarea"
	cran = "densityarea" 

	version("0.1.0", md5="f6c7e4b97630bd66ba3e6faa4f4bb64e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggdensity", type=("build", "run"))
	depends_on("r-isoband", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
