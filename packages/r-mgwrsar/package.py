# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgwrsar(RPackage):
	"""GWR and MGWR with Spatial Autocorrelation

	Functions for computing (Mixed) Geographically Weighted Regression with spatial autocorrelation, Geniaux and Martinetti (2017) <doi:10.1016/j.regsciurbeco.2017.04.001>.
	"""
	
	cran = "mgwrsar" 

	version("1.0.5", md5="dc5c2ae25125c2afb69aeb04542a2a4f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-spgwr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
