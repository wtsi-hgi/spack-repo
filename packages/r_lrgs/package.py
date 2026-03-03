# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrgs(RPackage):
	"""Linear Regression by Gibbs Sampling

	Implements a Gibbs sampler to do linear regression with multiple covariates, multiple responses, Gaussian measurement errors on covariates and responses, Gaussian intrinsic scatter, and a covariate prior distribution which is given by either a Gaussian mixture of specified size or a Dirichlet process with a Gaussian base distribution. Described further in Mantz (2016) <DOI:10.1093/mnras/stv3008>.
	"""
	
	homepage = "https://github.com/abmantz/lrgs"
	cran = "lrgs" 

	version("0.5.4", md5="94cc155b2feb61a9309231d2ad4342ce")

	depends_on("r-mvtnorm", type=("build", "run"))
