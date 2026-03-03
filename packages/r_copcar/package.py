# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopcar(RPackage):
	"""Fitting the copCAR Regression Model for Discrete Areal Data

	Provides tools for fitting the copCAR (Hughes, 2015)
    <DOI:10.1080/10618600.2014.948178> regression model for discrete
	areal data. Three types of estimation are supported (continuous
	extension, composite marginal likelihood, and distributional transform),
	for three types of outcomes (Bernoulli, negative binomial, and Poisson).
	"""
	
	cran = "copCAR" 

	version("2.0-4", md5="2994db905a7d7377d1ed6204d421bee8")

	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
