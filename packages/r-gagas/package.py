# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGagas(RPackage):
	"""Global Adaptive Generative Adjustment Algorithm for Generalized
Linear Models

	Fits linear regression, logistic and multinomial regression models, Poisson regression, Cox model via Global Adaptive Generative Adjustment Algorithm.  
 For more detailed information, see Bin Wang, Xiaofei Wang and Jianhua Guo (2022) <arXiv:1911.00658>. 
 This paper provides the theoretical properties of Gaga linear model when the load matrix is orthogonal. 
 Further study is going on for the nonorthogonal cases and generalized linear models. 
 These works are in part supported by the National Natural Foundation of China (No.12171076). 
	"""
	
	homepage = "https://arxiv.org/abs/1911.00658"
	cran = "GAGAs" 

	version("0.6.2", md5="11836485ec08449f0d28c1c2bc301445")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
