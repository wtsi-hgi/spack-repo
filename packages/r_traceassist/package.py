# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraceassist(RPackage):
	"""Nonparametric Trace Regression via Sign Series Representation

	Efficient method for fitting nonparametric matrix trace regression model. The detailed description can be found in  C. Lee, L. Li, H. Zhang, and M. Wang (2021). Nonparametric Trace Regression via Sign Series Representation. <arXiv:2105.01783>. The method employs the aggregation of structured sign series for trace regression (ASSIST) algorithm.
	"""
	
	homepage = "https://arxiv.org/abs/2105.01783"
	cran = "TraceAssist" 

	version("0.1.0", md5="1dbdf43baf3fd2f407f37f2419974081")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
