# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaeczi(RPackage):
	"""Small Area Estimation for Continuous Zero Inflated Data

	Provides functionality to fit a zero-inflated estimator for small area estimation.
    This estimator is a combines a linear mixed effects regression model and a logistic
    mixed effects regression model via a two-stage modeling approach. The estimator's mean
    squared error is estimated via a parametric bootstrap method. Chandra and others
    (2012, <doi:10.1080/03610918.2011.598991>) introduce and describe this estimator and mean
    squared error estimator. White and others (2024+, <arXiv:2402.03263>) describe the 
    applicability of this estimator to estimation of forest attributes and further assess the
    estimator's properties. 
	"""
	
	cran = "saeczi" 

	version("0.1.1", md5="07235f2f305883f4b2c9bf09ea8dbb95")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
