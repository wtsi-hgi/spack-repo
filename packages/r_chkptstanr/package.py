# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChkptstanr(RPackage):
	"""Checkpoint MCMC Sampling with 'Stan'

	Fit Bayesian models in Stan <doi: 10.18637/jss.v076.i01> 
  with checkpointing, that is, the ability to stop the MCMC sampler at 
  will, and then pick right back up where the MCMC sampler left off. 
  Custom 'Stan' models can be fitted, or the popular package 'brms' 
  <doi: 10.18637/jss.v080.i01> can be used to generate the 'Stan' code. This 
  package is fully compatible with the R packages 'brms', 'posterior', 'cmdstanr', 
  and 'bayesplot'. 
	"""
	
	cran = "chkptstanr" 

	version("0.1.1", md5="388d01c3615ca8509035a288e338b9a5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-brms@2.16.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
