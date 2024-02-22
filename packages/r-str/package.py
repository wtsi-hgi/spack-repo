# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStr(RPackage):
	"""STR Decomposition

	Methods for decomposing seasonal data: STR (a Seasonal-Trend decomposition procedure based on Regression) and Robust STR. In some ways, STR is similar to Ridge Regression and Robust STR can be related to LASSO. They allow for multiple seasonal components, multiple linear covariates with constant, flexible and seasonal influence. Seasonal patterns (for both seasonal components and seasonal covariates) can be fractional and flexible over time; moreover they can be either strictly periodic or have a more complex topology. The methods provide confidence intervals for the estimated components. The methods can be used for forecasting.
	"""
	
	homepage = "https://bitbucket.org/alexanderdokumentov/strpackage"
	cran = "stR" 

	version("0.6", md5="31287bb5844cd61e56f50b564a4d5e35")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
