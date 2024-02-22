# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBistablehistory(RPackage):
	"""Cumulative History Analysis for Bistable Perception Time Series

	Estimates cumulative history for time-series for continuously
    viewed bistable perceptual rivalry displays. Computes cumulative history
    via a homogeneous first order differential process. I.e., it assumes
    exponential growth/decay of the history as a function time and perceptually
    dominant state, Pastukhov & Braun (2011) <doi:10.1167/11.10.12>.
    Supports Gamma, log normal, and normal distribution families.
    Provides a method to compute history directly and example of using the
    computation on a custom Stan code.
	"""
	
	homepage = "https://github.com/alexander-pastukhov/bistablehistory/"
	cran = "bistablehistory" 

	version("1.1.2", md5="fbcd10db0d959f7fff4f5b8e94f6a124")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
