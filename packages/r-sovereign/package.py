# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSovereign(RPackage):
	"""State-Dependent Empirical Analysis

	A set of tools for state-dependent 
  empirical analysis through both VAR- and local projection-based 
  state-dependent forecasts, impulse response functions, 
  historical decompositions, and forecast error variance decompositions.   
	"""
	
	homepage = "https://github.com/tylerJPike/sovereign"
	cran = "sovereign" 

	version("1.2.1", md5="34c0122b6ceeb8ce6d21b198060839f6")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
