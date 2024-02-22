# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmls(RPackage):
	"""Gaussian Location-Scale Regression

	The Gaussian location-scale regression model is a multi-predictor
    model with explanatory variables for the mean (= location) and the standard
    deviation (= scale) of a response variable. This package implements maximum
    likelihood and Markov chain Monte Carlo (MCMC) inference (using algorithms
    from Girolami and Calderhead (2011) <doi:10.1111/j.1467-9868.2010.00765.x>
    and Nesterov (2009) <doi:10.1007/s10107-007-0149-x>), a parametric
    bootstrap algorithm, and diagnostic plots for the model class.
	"""
	
	homepage = "https://hriebl.github.io/lmls/"
	cran = "lmls" 

	version("0.1.0", md5="e08e53f2fd6c6f5160521f7a19d7528e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-generics@0.1:", type=("build", "run"))
