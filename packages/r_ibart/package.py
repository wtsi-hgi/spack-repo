# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbart(RPackage):
	"""Iterative Bayesian Additive Regression Trees Descriptor
Selection Method

	A statistical method based on Bayesian Additive Regression Trees with Global 
    Standard Error Permutation Test (BART-G.SE) for descriptor selection 
    and symbolic regression. It finds the symbolic formula of the regression function 
    y=f(x) as described in Ye, Senftle, and Li (2023) <arXiv:2110.10195>.
	"""
	
	homepage = "https://github.com/mattsheng/iBART"
	cran = "iBART" 

	version("1.0.0", md5="57b39827068cc964a1713252b2b6b835")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bartmachine@1.2.6:", type=("build", "run"))
	depends_on("r-glmnet@4.1.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
