# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbsp(RPackage):
	"""Multivariate Bayesian Model with Shrinkage Priors

	Gibbs sampler for fitting multivariate Bayesian linear regression with shrinkage priors (MBSP), using the three parameter beta normal family. The method is described in Bai and Ghosh (2018) <doi:10.1016/j.jmva.2018.04.010>. 
	"""
	
	cran = "MBSP" 

	version("4.0", md5="1107ad8366f8ccdbe7047c73812dfee3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
