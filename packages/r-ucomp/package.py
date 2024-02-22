# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcomp(RPackage):
	"""Automatic Unobserved Components and Other Time Series Models

	Comprehensive analysis and forecasting 
             of univariate time series using automatic 
             unobserved components models and algorithms.
             Harvey, AC (1989) <doi:10.1017/CBO9781107049994>.
             Pedregal DJ and Young PC (2002) <doi:10.1002/9780470996430>.
             Durbin J and Koopman SJ (2012) <doi:10.1093/acprof:oso/9780199641178.001.0001>.
             Hyndman RJ, Koehler AB, Ord JK, and Snyder RD (2008) <doi:10.1007/978-3-540-71918-2>.
	"""
	
	cran = "UComp" 

	version("4.0.2", md5="cb860d60f7cca12e39a43fc8f477f281")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-tsoutliers", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
