# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteppenal(RPackage):
	"""Stepwise Forward Variable Selection in Penalized Regression

	Model Selection Based on Combined Penalties. This package implements a stepwise forward variable selection algorithm based on a penalized likelihood criterion that combines the L0 with L2 or L1 norms.
	"""
	
	cran = "stepPenal" 

	version("0.2", md5="8552693d757b23825372910759e4f25d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-dfoptim", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
