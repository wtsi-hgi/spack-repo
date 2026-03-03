# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMte(RPackage):
	"""Maximum Tangent Likelihood Estimation for Robust Linear
Regression and Variable Selection

	Several robust estimators for linear regression and variable selection are provided. 
              Included are Maximum tangent likelihood estimator by Qin, et al., (2017) <arxiv:1708.05439>, 
              least absolute deviance estimator and Huber regression. The penalized version of each of these 
              estimator incorporates L1 penalty function, i.e., LASSO and Adaptive Lasso. They are able to 
              produce consistent estimates for both fixed and high-dimensional settings. 
	"""
	
	homepage = "GitHub:"
	cran = "MTE" 

	version("1.2", md5="249aaa0eb74dbd22210bc536aacca25f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rqpen", type=("build", "run"))
