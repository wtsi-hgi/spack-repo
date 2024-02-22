# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpfda(RPackage):
	"""Gaussian Process for Functional Data Analysis

	Functionalities for modelling functional data with 
    multidimensional inputs, multivariate functional data, and non-separable 
    and/or non-stationary covariance structure of function-valued processes. 
    In addition, there are functionalities for functional regression models where 
    the mean function depends on scalar and/or functional covariates and 
    the covariance structure depends on functional covariates. 
    The development version of the package can be found on 
    <https://github.com/gpfda/GPFDA-dev>.
	"""
	
	cran = "GPFDA" 

	version("3.1.3", md5="0d80aee7fb4a4aff58688b86c92e70e5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
