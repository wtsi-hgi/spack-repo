# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsdic(RPackage):
	"""Homogeneity and Sparsity Detection Incorporating Prior
Constraint Information

	We explore sparsity and homogeneity of regression coefficients incorporating prior constraint information. A general pairwise fusion approach is proposed to deal with the sparsity and homogeneity detection when combining prior convex constraints. We develop an modified alternating direction method of multipliers algorithm (ADMM) to obtain the estimators. 
	"""
	
	cran = "HSDiC" 

	version("0.1", md5="34b6b31e15911b3b92e577015f468735")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
