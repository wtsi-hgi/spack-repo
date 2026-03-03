# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenalizedclr(RPackage):
	"""Integrative Penalized Conditional Logistic Regression

	Implements L1 and L2 penalized conditional logistic regression with penalty 
    factors allowing for integration of multiple data sources. Implements
    stability selection for variable selection. 
	"""
	
	cran = "penalizedclr" 

	version("2.0.0", md5="0d060aa7be6b6e27c8b139f1f07f3ddd")

	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-clogitl1", type=("build", "run"))
