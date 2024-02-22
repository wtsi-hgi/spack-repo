# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscsurv(RPackage):
	"""Discrete Time Survival Analysis

	Provides data transformations, estimation utilities,
    predictive evaluation measures and simulation functions for discrete time
    survival analysis.
	"""
	
	cran = "discSurv" 

	version("2.0.0", md5="395a4fe3a438531cd7923c7612ab5b61")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-treeclust", type=("build", "run"))
	depends_on("r-functional", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
