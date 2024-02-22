# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopbasic(RPackage):
	"""General Bivariate Copula Theory and Many Utility Functions

	Extensive functions for bivariate copula (bicopula) computations and related operations 
 for bicopula theory. The lower, upper, product, and select other bicopula are implemented along 
 with operations including the diagonal, survival copula, dual of a copula, co-copula, and
 numerical bicopula density. Level sets, horizontal and vertical sections are supported. Numerical 
 derivatives and inverses of a bicopula are provided through which simulation is implemented. 
 Bicopula composition, convex combination, asymmetry extension, and products also are provided.
 Support extends to the Kendall Function as well as the Lmoments thereof. Kendall Tau,
 Spearman Rho and Footrule, Gini Gamma, Blomqvist Beta, Hoeffding Phi, Schweizer-
 Wolff Sigma, tail dependency, tail order, skewness, and bivariate Lmoments are implemented, and 
 positive/negative quadrant dependency, left (right) increasing (decreasing) are available. 
 Other features include Kullback-Leibler Divergence, Vuong Procedure, spectral measure, and 
 Lcomoments for inference, maximum likelihood, and AIC, BIC, and RMSE for goodness-of-fit. 
	"""
	
	cran = "copBasic" 

	version("2.2.3", md5="718e590dcba5b8f02fb4d5261ae1fb27")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
