# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnusualprofile(RPackage):
	"""Calculates Conditional Mahalanobis Distances

	Calculates a Mahalanobis distance for every row of a set of
    outcome variables (Mahalanobis, 1936
    <doi:10.1007/s13171-019-00164-5>). The conditional Mahalanobis
    distance is calculated using a conditional covariance matrix (i.e., a
    covariance matrix of the outcome variables after controlling for a set
    of predictors). Plotting the output of the cond_maha() function can
    help identify which elements of a profile are unusual after
    controlling for the predictors.
	"""
	
	homepage = "https://github.com/wjschne/unusualprofile"
	cran = "unusualprofile" 

	version("0.1.4", md5="341c2f0cb6365078fe09512b914edd7b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggnormalviolin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
