# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNse(RPackage):
	"""Numerical Standard Errors Computation in R

	Collection of functions designed to calculate numerical standard error (NSE) of univariate time series as described in Ardia et al. (2018) <doi:10.1515/jtse-2017-0011> and Ardia and Bluteau (2017) <doi:10.21105/joss.00172>.
	"""
	
	homepage = "https://github.com/keblu/nse"
	cran = "nse" 

	version("1.21", md5="74a99fa5197d8c6b331db7466306bd91")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mcmc", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
