# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmwmx(RPackage):
	"""Estimate Functional and Stochastic Parameters of Linear Models
with Correlated Residuals

	Implements the Generalized Method of Wavelet Moments with Exogenous Inputs estimator (GMWMX) presented in Cucci, D. A., Voirol, L., Kermarrec, G., Montillet, J. P., and Guerrier, S. (2023) <doi:10.1007/s00190-023-01702-8>.
             The GMWMX estimator allows to estimate functional and stochastic parameters of linear models with correlated residuals. 
             The 'gmwmx' package provides functions to estimate, compare and analyze models, utilities to load and work with Global Navigation Satellite System (GNSS) data as well as methods to compare results with the Maximum Likelihood Estimator (MLE) implemented in Hector.
	"""
	
	cran = "gmwmx" 

	version("1.0.3", md5="b2915cc01d894297335c388086bc215e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-wv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-longmemo", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-ltsa", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
