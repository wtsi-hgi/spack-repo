# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaximininfer(RPackage):
	"""Inference for Maximin Effects in High-Dimensional Settings

	Implementation of the sampling and aggregation method for the covariate shift maximin effect, which was proposed in <arXiv:2011.07568>. It constructs the confidence interval for any linear combination of the high-dimensional maximin effect.
	"""
	
	cran = "MaximinInfer" 

	version("2.0.0", md5="afce2e9160ddecc0bc1a7929b313ea21")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-sihr", type=("build", "run"))
