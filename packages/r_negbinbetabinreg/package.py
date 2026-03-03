# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNegbinbetabinreg(RPackage):
	"""Negative Binomial and Beta Binomial Bayesian Regression Models

	The Negative Binomial regression with mean and shape modeling and mean and variance modeling and Beta Binomial regression with mean and dispersion modeling.
	"""
	
	cran = "NegBinBetaBinreg" 

	version("1.0", md5="9c5d9b6a823c0885ab427844e0d1fda5")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
