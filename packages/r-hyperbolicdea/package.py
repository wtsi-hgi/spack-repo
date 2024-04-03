# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperbolicdea(RPackage):
	"""Hyperbolic DEA Estimation

	Implements Data Envelopment Analysis (DEA) with a hyperbolic orientation using a non-linear programming solver. It enables flexible estimations with weight restrictions, non-discretionary variables, and a generalized distance function. Additionally, it allows for the calculation of slacks and super-efficiency scores. The methods are detailed in Öttl et al. (2023), <doi:10.1016/j.dajour.2023.100343>. Furthermore, the package provides a non-linear profitability estimation built upon the DEA framework. 
	"""
	
	cran = "hyperbolicDEA" 

	version("1.0.0", md5="e6977e3a122898c072ed0571adee8b22")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
