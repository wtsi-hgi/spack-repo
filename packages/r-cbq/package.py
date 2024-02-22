# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbq(RPackage):
	"""Conditional Binary Quantile Models

	Estimates conditional binary quantile models developed by Lu (2020) <doi:10.1017/pan.2019.29>. The estimation procedure is implemented based on Markov chain Monte Carlo methods. 
	"""
	
	cran = "cbq" 

	version("0.2.0.3", md5="419522f696a99f23cb146228bf0615f8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
