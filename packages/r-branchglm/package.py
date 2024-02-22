# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBranchglm(RPackage):
	"""Efficient Best Subset Selection for GLMs via Branch and Bound
Algorithms

	Performs efficient and scalable glm best 
	subset selection using a novel implementation of a branch and bound algorithm.
	To speed up the model fitting process, a range of optimization
	methods are implemented in 'RcppArmadillo'. Parallel computation 
	is available using 'OpenMP'.
	"""
	
	homepage = "https://github.com/JacobSeedorff21/BranchGLM"
	cran = "BranchGLM" 

	version("2.1.4", md5="bf1ba46c7e8312d0016d6bcf7e7407f3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
