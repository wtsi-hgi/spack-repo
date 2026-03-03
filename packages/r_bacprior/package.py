# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacprior(RPackage):
	"""Choice of Omega in the BAC Algorithm

	The Bayesian Adjustment for Confounding (BAC) algorithm (Wang et al., 2012)
 can be used to estimate the causal effect of a continuous exposure on a continuous outcome.
 This package provides an approximate sensitivity analysis of BAC with regards to the
 hyperparameter omega. BACprior also provides functions to guide the user in their choice
 of an appropriate omega value. The method is based on Lefebvre, Atherton and Talbot (2014).
	"""
	
	cran = "BACprior" 

	version("2.1.1", md5="914c35ef1d6d59ec17d54f83282ed453")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
