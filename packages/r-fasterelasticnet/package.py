# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasterelasticnet(RPackage):
	"""An Amazing Fast Way to Fit Elastic Net

	Fit Elastic Net, Lasso, and Ridge regression and do cross-validation in a fast way. We build the algorithm based on Least Angle Regression by Bradley Efron, Trevor Hastie, Iain Johnstone, etc. (2004)(<doi:10.1214/009053604000000067 >) and some algorithms like Givens rotation and Forward/Back Substitution. In this way, many matrices to be computed are retained as triangular matrices which can eventually speed up the computation. The fitting algorithm for Elastic Net is written in C++ using Armadillo linear algebra library.
	"""
	
	homepage = "https://github.com/CUFESAM/Elastic-Net"
	cran = "fasterElasticNet" 

	version("1.1.2", md5="eb460e01cdf2f965ea6a0881322aeeeb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
