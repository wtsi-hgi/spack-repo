# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrlmm(RPackage):
	"""Quantile Regression for Linear Mixed-Effects Models

	Quantile regression (QR) for Linear 
             Mixed-Effects Models via the asymmetric Laplace distribution (ALD). 
             It uses the Stochastic Approximation of the EM (SAEM) algorithm for 
             deriving exact maximum likelihood estimates and full inference results 
             for the fixed-effects and variance components. 
             It also provides graphical summaries for assessing the algorithm 
             convergence and fitting results.
	"""
	
	cran = "qrLMM" 

	version("2.2", md5="ce61287a504093fcee733efab754deba")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-lqr", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-ald", type=("build", "run"))
