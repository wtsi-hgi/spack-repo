# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalcop(RPackage):
	"""Local Likelihood Inference for Conditional Copula Models

	Implements a local likelihood estimator for the dependence parameter in bivariate conditional copula models.  Copula family and local likelihood bandwidth parameters are selected by leave-one-out cross-validation.  The models are implemented in 'TMB', meaning that the local score function is efficiently calculated via automated differentiation (AD), such that quasi-Newton algorithms may be used for parameter estimation.
	"""
	
	homepage = "https://github.com/mlysy/LocalCop"
	cran = "LocalCop" 

	version("0.0.1", md5="9b47273991628b6bfb0fa3a07be57210")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
