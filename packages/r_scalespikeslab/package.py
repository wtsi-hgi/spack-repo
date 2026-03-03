# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScalespikeslab(RPackage):
	"""Scalable Spike-and-Slab

	A scalable Gibbs sampling implementation for high dimensional Bayesian regression with the continuous spike-and-slab prior. Niloy Biswas, Lester Mackey and Xiao-Li Meng, "Scalable Spike-and-Slab" (2022) <arXiv:2204.01668>.
	"""
	
	cran = "ScaleSpikeSlab" 

	version("1.0", md5="ef2d0479a50f4f5df0f51ea258ef0079")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
