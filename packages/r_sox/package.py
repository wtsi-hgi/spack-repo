# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSox(RPackage):
	"""Structured Learning in Time-Dependent Cox Models

	Efficient procedures for fitting and cross-validating the structurally-regularized time-dependent Cox models.
	"""
	
	cran = "sox" 

	version("1.1", md5="e2caff7281b4c0ef7bdc3faf66a3e6ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
