# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChisquare(RPackage):
	"""Chi-Square and G-Square Test of Independence, Power and Residual
Analysis, Measures of Categorical Association

	Provides the facility to perform the chi-square and G-square test of independence, calculates the power of the traditional chi-square test, compute permutation and Monte Carlo p-value, and provides measures of association such as Phi, odds ratio with 95 percent CI and p-value, adjusted contingency coefficient, Cramer's V and 95 percent CI, bias-corrected Cramer's V, W, Cohen's w, Goodman-Kruskal's lambda, gamma and its p-value, and tau, Cohen's k and its 95 percent CI. It also calculates standardized, moment-corrected standardized, and adjusted standardized residuals, and their significance. Different outputs are returned in nicely formatted tables.
	"""
	
	cran = "chisquare" 

	version("0.9", md5="1884610a61ea88d5209280d3db9b717d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gt@0.3.1:", type=("build", "run"))
