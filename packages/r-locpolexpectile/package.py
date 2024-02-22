# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocpolexpectile(RPackage):
	"""Local Polynomial Expectile Regression

	Provides the local polynomial expectile regression method and different bandwidth selection procedures. The codes include local polynomial univariate expectile regression with several data-driven methods for bandwidth selection; local linear bivariate and trivariate expectile regression; and partially linear expectile regression, allowing for different errors structures (homoscedastic error and various heteroscedastic error structures). For more details, see Adam and Gijbels (2021a) <doi:10.1007/s10463-021-00799-y> and Adam and Gijbels (2021b) <doi:10.1007/978-3-030-73249-3_8>.
	"""
	
	cran = "locpolExpectile" 

	version("0.1.1", md5="d485b43ee2bd93e0db0a5347282b6b3d")

	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-expectreg", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-lestat", type=("build", "run"))
