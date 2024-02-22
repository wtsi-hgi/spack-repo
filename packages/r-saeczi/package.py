# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaeczi(RPackage):
	"""Small Area Estimation for Continuous Zero Inflated Data

	Simplifies the process of fitting a zero-inflated estimator
    onto a dataset. This estimator is a combination of a linear mixed effects regression model 
    and a logistic mixed effects regression model which is summarized by White and others (2024, <arXiv:2402.03263>).
    The variance is estimated through a parametric bootstrapping method which is given 
    by Chandra and others (2012, <doi:10.1080/03610918.2011.598991>). 
	"""
	
	cran = "saeczi" 

	version("0.1.0", md5="e51c51d1b71834317b41d8eece43e335")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
