# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGjrm(RPackage):
	"""Generalised Joint Regression Modelling

	Routines for fitting various joint (and univariate) regression models, with several types of covariate effects, in the presence of equations' errors association, endogeneity, non-random sample selection or partial observability.
	"""
	
	homepage = "https://www.ucl.ac.uk/statistics/people/giampieromarra"
	cran = "GJRM" 

	version("0.2-6.5", md5="77ed6d5a04610dcbbc695bab4d689bf2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-ismev", type=("build", "run"))
