# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGinidecomply(RPackage):
	"""Gini Decomposition by Income Sources

	Estimation of the effect of each income source on income inequalities based on the decomposition of Lerman and Yitzhaki (1985) <doi:10.2307/1928447>. 
	"""
	
	cran = "GiniDecompLY" 

	version("1.0.0", md5="31733081c3de8f3b50e0b7a16229664d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
