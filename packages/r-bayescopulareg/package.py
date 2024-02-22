# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayescopulareg(RPackage):
	"""Bayesian Copula Regression

	Tools for Bayesian copula generalized linear models (GLMs). 
             The sampling scheme is based on Pitt, Chan, and Kohn (2006) <doi:10.1093/biomet/93.3.537>. 
             Regression parameters (including coefficients and dispersion parameters) are
             estimated via the adaptive random walk Metropolis approach developed by
             Haario, Saksman, and Tamminen (1999) <doi:10.1007/s001800050022>.
             The prior for the correlation matrix is based on Hoff (2007) <doi:10.1214/07-AOAS107>.
	"""
	
	homepage = "https://github.com/ethan-alt/bayescopulareg"
	cran = "bayescopulareg" 

	version("0.1.3", md5="339a57bde79e5d029c17b83b7dd68d07")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
