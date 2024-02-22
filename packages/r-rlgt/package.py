# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlgt(RPackage):
	"""Bayesian Exponential Smoothing Models with Trend Modifications

	An implementation of a number of Global Trend models for time series forecasting 
    that are Bayesian generalizations and extensions of some Exponential Smoothing models. 
    The main differences/additions include 1) nonlinear global trend, 2) Student-t error 
    distribution, and 3) a function for the error size, so heteroscedasticity. The methods 
    are particularly useful for short time series. When tested on the well-known M3 dataset,
    they are able to outperform all classical time series algorithms. The models are fitted 
    with MCMC using the 'rstan' package.
	"""
	
	homepage = "https://github.com/cbergmeir/Rlgt"
	cran = "Rlgt" 

	version("0.2-1", md5="fcb197dd8a967020bd853239891562d6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
