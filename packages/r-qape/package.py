# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQape(RPackage):
	"""Quantile of Absolute Prediction Errors

	Estimates QAPE using bootstrap procedures. The residual, parametric and double bootstrap is used. The test of normality using Cholesky decomposition is added. Y pop is defined.
	"""
	
	cran = "qape" 

	version("2.1", md5="2c7f40c66552513ed2877a47bbb3cbe4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
