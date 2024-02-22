# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickregression(RPackage):
	"""Quick Linear Regression

	Helps to perform linear regression analysis by reducing manual effort. Reduces the independent variables based on specified p-value and Variance Inflation Factor (VIF) level.
	"""
	
	cran = "quickregression" 

	version("0.2", md5="32b25862c36ced2be7c1a56b987ead4e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-car@2.1:", type=("build", "run"))
