# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxplus(RPackage):
	"""Cox Regression (Proportional Hazards Model) with Multiple Causes
and Mixed Effects

	A high performance package estimating Cox Model when an even has more than one causes. It also supports random and fixed effects, tied events, and time-varying variables.
	"""
	
	cran = "CoxPlus" 

	version("1.1.1", md5="15b7b36a19e80b147c8a5e92b72202b5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
