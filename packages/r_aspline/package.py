# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspline(RPackage):
	"""Spline Regression with Adaptive Knot Selection

	Perform one-dimensional spline regression with automatic knot selection.
      This package uses a penalized approach to select the most relevant knots.
      B-splines of any degree can be fitted. More details in 'Goepp et al. (2018)',
      "Spline Regression with Automatic Knot Selection", <arXiv:1808.01770>.
	"""
	
	homepage = "https://github.com/goepp/aspline"
	cran = "aspline" 

	version("0.2.0", md5="f89454c0d7cc97dc70937dc0ca0e07eb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
