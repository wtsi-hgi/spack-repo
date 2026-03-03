# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamdit(RPackage):
	"""Bayesian Meta-Analysis of Diagnostic Test Data

	Provides a new class of Bayesian meta-analysis models that incorporates a model for internal and external validity bias. In this way, it is possible to combine studies of diverse quality and different types. For example, we can combine the results of randomized control trials (RCTs) with the results of observational studies (OS). 
	"""
	
	cran = "bamdit" 

	version("3.4.0", md5="e45f8890994ea0bae97944a72c99eb02")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rjags@4:", type=("build", "run"))
	depends_on("r-r2jags@0.4.03:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
