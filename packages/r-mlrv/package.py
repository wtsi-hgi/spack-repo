# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlrv(RPackage):
	"""Long-Run Variance Estimation in Time Series Regression

	Plug-in and difference-based long-run covariance matrix estimation for time series regression. Two applications of hypothesis testing are also provided. The first one is for testing for structural stability in coefficient functions. The second one is aimed at detecting long memory in time series regression. 
	"""
	
	cran = "mlrv" 

	version("0.1.1", md5="d2d1986a8103f24ebf0265b114126d3f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
