# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLnirt(RPackage):
	"""LogNormal Response Time Item Response Theory Models

	Allows the simultaneous analysis of responses and response times in an Item Response Theory (IRT) modelling framework. Supports variable person speed functions (intercept, trend, quadratic), and covariates for item and person (random) parameters. Data missing-by-design can be specified. Parameter estimation is done with a MCMC algorithm. LNIRT replaces the package CIRT, which was written by Rinke Klein Entink. For reference, see the paper by Fox, Klein Entink and Van der Linden (2007), "Modeling of Responses and Response Times with the Package cirt", Journal of Statistical Software, <doi:10.18637/jss.v020.i07>.
	"""
	
	cran = "LNIRT" 

	version("0.5.1", md5="6ed776a692cf656cc0a6bf05c99d879a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
