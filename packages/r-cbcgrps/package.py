# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbcgrps(RPackage):
	"""Compare Baseline Characteristics Between Groups

	Compare baseline characteristics between two or more groups. The variables being compared can be factor and numeric variables. The function will automatically judge the type and distribution of the variables, and make statistical description and bivariate analysis. 
	"""
	
	cran = "CBCgrps" 

	version("2.8.2", md5="0e14d52fff6f914da4a1ca0a8e05c9fe")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nortest@1.0.4:", type=("build", "run"))
