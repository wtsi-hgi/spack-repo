# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndependenceweights(RPackage):
	"""Estimates Weights for Confounding Control for Continuous-Valued
Exposures

	Estimates weights to make a continuous-valued exposure statistically independent of a vector of pre-treatment covariates using the method proposed in Huling, Greifer, and Chen (2021) <arxiv:2107.07086>. 
	"""
	
	cran = "independenceWeights" 

	version("0.0.1", md5="415bd3caa7c750c186324260ef833b5c")

	depends_on("r-osqp@0.6.0.3:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
