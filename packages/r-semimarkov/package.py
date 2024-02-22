# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemimarkov(RPackage):
	"""Multi-States Semi-Markov Models

	Functions for fitting multi-state semi-Markov models to longitudinal data. A parametric maximum likelihood estimation method adapted to deal with Exponential, Weibull and Exponentiated Weibull distributions is considered. Right-censoring can be taken into account and both constant and time-varying covariates can be included using a Cox proportional model. Reference: A. Krol and P. Saint-Pierre (2015) 	<doi:10.18637/jss.v066.i06>.
	"""
	
	cran = "SemiMarkov" 

	version("1.4.6", md5="b7fe6b5d1fbceece3ed3fb694de7cd5f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
