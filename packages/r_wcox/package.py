# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcox(RPackage):
	"""Weights to Correct for Outcome Dependent Sampling in Time to
Event Data

	A new inverse probability of selection weighted Cox model to deal with outcome-dependent sampling in survival analysis.
	"""
	
	cran = "wcox" 

	version("1.0", md5="3fa68f69d0ccaa3d350402dd2ba659f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
