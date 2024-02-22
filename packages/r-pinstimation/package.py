# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinstimation(RPackage):
	"""Estimation of the Probability of Informed Trading

	A comprehensive bundle of utilities for the estimation of probability of informed trading models: original PIN in Easley and O'Hara (1992) and Easley et al. (1996); Multilayer PIN (MPIN) in Ersan (2016); Adjusted PIN (AdjPIN) in Duarte and Young (2009); and volume-synchronized PIN (VPIN) in Easley et al. (2011, 2012). Implementations of various estimation methods suggested in the literature are included. Additional compelling features comprise posterior probabilities, an implementation of an expectation-maximization (EM) algorithm, and PIN decomposition into layers, and into bad/good components. Versatile data simulation tools, and trade classification algorithms are among the supplementary utilities. The package provides fast, compact, and precise utilities to tackle the sophisticated, error-prone, and time-consuming estimation procedure of informed trading, and this solely using the raw trade-level data. 
	"""
	
	homepage = "https://www.pinstimation.com"
	cran = "PINstimation" 

	version("0.1.2", md5="b5e190bd35e370fbae65c88a4977a080")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-skellam", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
