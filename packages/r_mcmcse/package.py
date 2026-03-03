# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcse(RPackage):
	"""Monte Carlo Standard Errors for MCMC

	Provides tools for computing Monte Carlo standard
        errors (MCSE) in Markov chain Monte Carlo (MCMC) settings. MCSE
        computation for expectation and quantile estimators is
        supported as well as multivariate estimations. The package also provides 
	functions for computing effective sample size and for plotting
	Monte Carlo estimates versus sample size.
	"""
	
	cran = "mcmcse" 

	version("1.5-0", md5="52bc8e299119ae4209615a9a107250ba")

	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fftwtools", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
