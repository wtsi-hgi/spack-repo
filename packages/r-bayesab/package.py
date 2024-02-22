# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesab(RPackage):
	"""Fast Bayesian Methods for AB Testing

	A suite of functions that allow the user to analyze A/B test
    data in a Bayesian framework. Intended to be a drop-in replacement for
    common frequentist hypothesis test such as the t-test and chi-sq test.
	"""
	
	homepage = "https://github.com/FrankPortman/bayesAB"
	cran = "bayesAB" 

	version("1.1.3", md5="8d8b374c526112166846e13746ee0dfd")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
