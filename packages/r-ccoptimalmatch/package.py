# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcoptimalmatch(RPackage):
	"""Implementation of Case-Control Optimal Matching

	Cases are matched to controls in an efficient, optimal and computationally flexible way. It uses 
             the idea of sub-sampling in the level of the case, by creating pseudo-observations of controls. The 
             user can select between replacement and without replacement, the number of controls, and several covariates 
             to match upon. See Mamouris (2021) <doi:10.1186/s12874-021-01256-3> for an overview.
	"""
	
	cran = "ccoptimalmatch" 

	version("0.1.0", md5="067804442ab74ac6b7539f418a3dcd53")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
