# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrnlmm(RPackage):
	"""Quantile Regression for Nonlinear Mixed-Effects Models

	Quantile regression (QR) for Nonlinear
             Mixed-Effects Models via the asymmetric Laplace distribution (ALD). 
             It uses the Stochastic Approximation of the EM (SAEM) algorithm for 
             deriving exact maximum likelihood estimates and full inference results 
             for the fixed-effects and variance components.
             It also provides prediction and graphical summaries for assessing the algorithm
             convergence and fitting results.
	"""
	
	cran = "qrNLMM" 

	version("3.3", md5="047ee62889a5856a84f1484cf3c6c363")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lqr", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-ald", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
