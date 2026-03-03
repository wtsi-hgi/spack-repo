# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsmousetrack(RPackage):
	"""Bayesian State-Space Modeling of Mouse-Tracking Experiments via
Stan

	Estimates previously compiled state-space modeling for mouse-tracking experiments using the 'rstan' package, which provides the R interface to the Stan C++ library for Bayesian estimation.
	"""
	
	cran = "ssMousetrack" 

	version("1.1.6", md5="9743424687438398b4c0046d856231b9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-rstan@2.18.2:", type=("build", "run"))
	depends_on("r-rstantools@1.5.1:", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
