# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmeta(RPackage):
	"""Bayesian Random-Effects Meta-Analysis and Meta-Regression

	A collection of functions allowing to derive the posterior distribution of the model parameters in random-effects meta-analysis or meta-regression, and providing functionality to evaluate joint and marginal posterior probability distributions, predictive distributions, shrinkage effects, posterior predictive p-values, etc.; For more details, see also Roever C (2020) <doi:10.18637/jss.v093.i06>, or Roever C and Friede T (2022) <doi:10.1016/j.cmpb.2022.107303>.
	"""
	
	homepage = "https://gitlab.gwdg.de/croever/bayesmeta"
	cran = "bayesmeta" 

	version("3.4", md5="9b3352a1d31cbe5feaf87267232d0d28")

	depends_on("r-forestplot@2:", type=("build", "run"))
	depends_on("r-metafor@2.0.0:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.1:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
