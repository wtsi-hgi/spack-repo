# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehbZib(RPackage):
	"""Small Area Estimation using Hierarchical Bayesian under Zero
Inflated Binomial Distribution

	Provides function for area level of small area estimation using hierarchical Bayesian (HB) method with Zero-Inflated Binomial distribution for variables of interest. Some dataset produced by a data generation are also provided. The 'rjags' package is employed to obtain parameter estimates. Model-based estimators involves the HB estimators which include the mean and the variation of mean.
	"""
	
	cran = "saeHB.ZIB" 

	version("0.1.1", md5="7d52ab0db131864d4bc9f946b7e6a991")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
