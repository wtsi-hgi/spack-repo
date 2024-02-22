# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHolodeck(RPackage):
	"""A Tidy Interface for Simulating Multivariate Data

	Provides pipe-friendly (%>%) wrapper functions for MASS::mvrnorm() to create simulated multivariate data sets
    with groups of variables with different degrees of variance, covariance, and effect size. 
	"""
	
	homepage = "https://github.com/Aariq/holodeck"
	cran = "holodeck" 

	version("0.2.2", md5="c95009a6c0b9672cf00eeb5f207163c0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
