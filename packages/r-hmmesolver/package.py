# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmesolver(RPackage):
	"""A Fast Solver for Henderson Mixed Model Equation via Row
Operations

	Consider the linear mixed model with normal random effects. A typical method to solve Henderson's Mixed Model Equations (HMME) is recursive estimation of the fixed effects and random effects. We provide a fast, stable, and scalable solver to the HMME without computing matrix inverse. See Kim (2017) <arXiv:1710.09663> for more details.
	"""
	
	cran = "HMMEsolver" 

	version("0.1.2", md5="6e48f0d17779f78ac377263fb462b0cd")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
