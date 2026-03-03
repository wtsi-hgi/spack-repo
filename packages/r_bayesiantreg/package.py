# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesiantreg(RPackage):
	"""Bayesian t Regression for Modeling Mean and Scale Parameters

	Performs Bayesian t Regression where mean and scale parameters are modeling by lineal regression structures, and the degrees of freedom parameters are estimated. 
	"""
	
	cran = "Bayesiantreg" 

	version("1.0.1", md5="6271faa93bd04af194f2607e66b13e35")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1:", type=("build", "run"))
