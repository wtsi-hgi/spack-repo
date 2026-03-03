# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJarbes(RPackage):
	"""Just a Rather Bayesian Evidence Synthesis

	Provides a new class of Bayesian meta-analysis models that incorporates a model for internal and external validity bias. In this way, it is possible to combine studies of diverse quality and different types. For example, we can combine the results of randomized control trials (RCTs) with the results of observational studies (OS). 
	"""
	
	cran = "jarbes" 

	version("2.0.0", md5="2e130f7956bedb879569bb15b1b86b6b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rjags@4:", type=("build", "run"))
	depends_on("r-r2jags@0.4.03:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mcmcplots", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
