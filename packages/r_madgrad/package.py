# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadgrad(RPackage):
	"""'MADGRAD' Method for Stochastic Optimization

	A Momentumized, Adaptive, Dual Averaged Gradient Method for Stochastic 
  Optimization algorithm. MADGRAD is a 'best-of-both-worlds' optimizer with the 
  generalization performance of stochastic gradient descent and at least as fast 
  convergence as that of Adam, often faster. A drop-in optim_madgrad() implementation
  is provided based on Defazio et al (2020) <arxiv:2101.11075>.
	"""
	
	cran = "madgrad" 

	version("0.1.0", md5="f426b8d2e3a6bb4898e06efd6c1ed972")

	depends_on("r-torch@0.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
