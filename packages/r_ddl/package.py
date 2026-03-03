# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdl(RPackage):
	"""Doubly Debiased Lasso (DDL)

	Statistical inference for the regression coefficients in high-dimensional linear models with hidden confounders. The Doubly Debiased Lasso method was proposed in <arXiv:2004.03758>.
	"""
	
	cran = "DDL" 

	version("1.0.2", md5="dc62c53de3cca84180e997fe3f6e9f58")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
