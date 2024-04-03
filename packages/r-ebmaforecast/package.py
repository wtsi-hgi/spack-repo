# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbmaforecast(RPackage):
	"""Estimate Ensemble Bayesian Model Averaging Forecasts using Gibbs
Sampling or EM-Algorithms

	Create forecasts from multiple predictions using ensemble Bayesian model averaging (EBMA). EBMA models can be estimated using an expectation maximization (EM) algorithm or as fully Bayesian models via Gibbs sampling. The methods in this package are Montgomery, Hollenbach, and Ward (2015) <doi:10.1016/j.ijforecast.2014.08.001> and Montgomery, Hollenbach, and Ward (2012) <doi:10.1093/pan/mps002>.
	"""
	
	homepage = "https://github.com/fhollenbach/EBMA/"
	cran = "EBMAforecast" 

	version("1.0.31", md5="c35d19a4f67de8624301175ba840eeb7")
	version("1.0.32", md5="9d0a24db4680ec2bc5a8261c9ae7a5be")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-separationplot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
