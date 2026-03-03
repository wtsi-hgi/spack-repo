# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhantsem(RPackage):
	"""Create Phantom Variables in Structural Equation Models for
Sensitivity Analyses

	Create phantom variables, which are variables that were not observed, for the purpose of sensitivity analyses for structural equation models. The package makes it easier for a user to test different combinations of covariances between the phantom variable(s) and observed variables. The package may be used to assess a model's or effect's sensitivity to temporal bias (e.g., if cross-sectional data were collected) or confounding bias. 
	"""
	
	cran = "phantSEM" 

	version("1.0.0.0", md5="2f195be60ed2f636b2317c13a4d7b8fa")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
	depends_on("r-lavaan@0.6.11:", type=("build", "run"))
