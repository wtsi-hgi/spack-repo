# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebpower(RPackage):
	"""Basic and Advanced Statistical Power Analysis

	This is a collection of tools for conducting both basic and advanced statistical power analysis including correlation, proportion, t-test, one-way ANOVA, two-way ANOVA, linear regression, logistic regression, Poisson regression, mediation analysis, longitudinal data analysis, structural equation modeling and multilevel modeling. It also serves as the engine for conducting power analysis online at <https://webpower.psychstat.org>.
	"""
	
	homepage = "https://webpower.psychstat.org"
	cran = "WebPower" 

	version("0.9.4", md5="be2288e3c8476d850d708c3d485d7b59")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-pearsonds", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
