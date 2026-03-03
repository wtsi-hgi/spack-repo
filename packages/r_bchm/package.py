# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBchm(RPackage):
	"""Clinical Trial Calculation Based on BCHM Design

	Users can estimate the treatment effect for multiple subgroups basket trials based on the Bayesian Cluster Hierarchical Model (BCHM). In this model, a Bayesian non-parametric method is applied to dynamically calculate the number of clusters by conducting the multiple cluster classification based on subgroup outcomes. Hierarchical model is used to compute the posterior probability of treatment effect with the borrowing strength determined by the Bayesian non-parametric clustering and the similarities between subgroups. To use this package, 'JAGS' software and 'rjags' package are required, and users need to pre-install them.
	"""
	
	cran = "BCHM" 

	version("1.00", md5="25de37ab379c18536a388bc26d357c89")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("jags", type=("build", "link", "run"))
