# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenlasso(RPackage):
	"""Path Algorithm for Generalized Lasso Problems

	Computes the solution path for generalized lasso problems. Important use cases are the fused lasso over an arbitrary graph, and trend fitting of any given polynomial order. Specialized implementations for the latter two subproblems are given to improve stability and speed. See Taylor Arnold and Ryan Tibshirani (2016) <doi:10.1080/10618600.2015.1008638>.
	"""
	
	homepage = "https://github.com/glmgen/genlasso"
	cran = "genlasso" 

	version("1.6.1", md5="f206584297fe188a468438103ba42bbb")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
