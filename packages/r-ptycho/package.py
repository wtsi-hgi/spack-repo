# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtycho(RPackage):
	"""Bayesian Variable Selection with Hierarchical Priors

	
  Bayesian variable selection for linear regression models using hierarchical
  priors. There is a prior that combines information across responses and one
  that combines information across covariates, as well as a standard spike and
  slab prior for comparison. An MCMC samples from the marginal posterior
  distribution for the 0-1 variables indicating if each covariate belongs to the
  model for each response.
	"""
	
	homepage = "web.stanford.edu/~lstell/ptycho/"
	cran = "ptycho" 

	version("1.1-4", md5="8d44723aacb6fa1477a25b94230db60e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
