# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvek(RPackage):
	"""Cross-Validated Kernel Ensemble

	
  Implementation of Cross-Validated Kernel Ensemble (CVEK), 
  a flexible modeling framework for robust nonlinear regression and 
  hypothesis testing based on ensemble learning with kernel-ridge estimators 
  (Jeremiah et al. (2017) <arXiv:1710.01406> and 
  Wenying et al. (2018) <arXiv:1811.11025>). It allows user to conduct 
  nonlinear regression with minimal assumption on the function form by 
  aggregating nonlinear models generated from a diverse collection of kernel 
  families. It also provides utilities to test for the estimated nonlinear 
  effect under this ensemble estimator, using either the asymptotic or 
  the bootstrap version of a generalized score test.
	"""
	
	cran = "CVEK" 

	version("0.1-2", md5="21d343b3fd739438ce6b02cf1b83ddea")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
