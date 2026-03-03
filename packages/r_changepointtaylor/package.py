# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointtaylor(RPackage):
	"""Identify Changes in Mean

	A basic implementation of the change in mean detection method outlined in: Taylor, Wayne A. (2000) <https://variation.com/wp-content/uploads/change-point-analyzer/change-point-analysis-a-powerful-new-tool-for-detecting-changes.pdf>. The package recursively uses the mean-squared error change point calculation to identify candidate change points. The candidate change points are then re-estimated and Taylor's backwards elimination process is then employed to come up with a final set of change points. Many of the underlying functions are written in C++ for improved performance. 
	"""
	
	cran = "ChangePointTaylor" 

	version("0.2", md5="21dc00cb3821a41925266c0adf9de7b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-bench", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
