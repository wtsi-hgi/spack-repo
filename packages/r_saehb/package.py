# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaehb(RPackage):
	"""Small Area Estimation using Hierarchical Bayesian Method

	Provides several functions for area level of small area estimation using hierarchical Bayesian (HB) methods with several univariate distributions for variables of interest. The dataset that is used in every function is generated accordingly in the Example. The 'rjags' package is employed to obtain parameter estimates. Model-based estimators involve the HB estimators which include the mean and the variation of mean. For the reference, see Rao and Molina (2015) <doi:10.1002/9781118735855>.
	"""
	
	homepage = "https://github.com/zazaperwira/saeHB"
	cran = "saeHB" 

	version("0.2.2", md5="2e53a78a5b7ed2165c5d1b7b1c0299f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
	depends_on("r-carbayesdata", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
