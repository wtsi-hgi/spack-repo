# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrops(RPackage):
	"""Changepoints for a Range of Penalties (CROPS)

	Implements the Changepoints for a Range of Penalties (CROPS) algorithm of Haynes et al. (2017) <doi:10.1080/10618600.2015.1116445> for finding all of the optimal segmentations for multiple penalty values over a continuous range.
	"""
	
	cran = "crops" 

	version("1.0.3", md5="b55da8bd970b97f1a56276e1e2615567")

	depends_on("r-sets", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
