# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdprior(RPackage):
	"""Scale-Dependent Hyperpriors in Structured Additive
Distributional Regression

	Utility functions for scale-dependent and alternative hyperpriors. The distribution parameters may capture location, scale, shape, etc. and every parameter may depend
  on complex additive terms (fixed, random, smooth, spatial, etc.) similar to a generalized additive model. Hyperpriors for all effects can be elicitated within the package. Including complex tensor product interaction terms and variable selection priors. The basic model is explained in in Klein and Kneib (2016) <doi:10.1214/15-BA983>.
	"""
	
	cran = "sdPrior" 

	version("1.0-0", md5="dc06c0753c1721d40e3db34a71940cdd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gb2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
