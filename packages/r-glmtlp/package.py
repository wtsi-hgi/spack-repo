# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmtlp(RPackage):
	"""Generalized Linear Models with Truncated Lasso Penalty

	Extremely efficient procedures for fitting regularization path with l0, l1, and truncated lasso penalty for linear regression and logistic regression models. This version is a completely new version compared with our previous version, which was mainly based on R. New core algorithms are developed and are now written in C++ and highly optimized. 
	"""
	
	homepage = "https://yuyangyy.com/glmtlp/"
	cran = "glmtlp" 

	version("2.0.1", md5="e1f800fa6f77e81bdec8c8433a1e1d99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
