# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlassosurvic(RPackage):
	"""Adaptive Lasso for the Cox Regression with Interval Censored and
Possibly Left Truncated Data

	Penalized variable selection tools for the Cox 
    proportional hazards model with interval censored and possibly 
    left truncated data. It performs variable selection via 
    penalized nonparametric maximum likelihood estimation with an 
    adaptive lasso penalty. The optimal thresholding parameter can be 
    searched by the package based on the profile Bayesian information 
    criterion (BIC). The asymptotic validity of the methodology is 
    established in Li et al. (2019 <doi:10.1177/0962280219856238>). 
    The unpenalized nonparametric maximum likelihood estimation for 
    interval censored and possibly left truncated data is also 
    available.
	"""
	
	cran = "ALassoSurvIC" 

	version("0.1.1", md5="d5bad14106668bb5a93010939c8c417b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
