# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInjurytools(RPackage):
	"""A Toolkit for Sports Injury Data Analysis

	Sports Injury Data analysis aims to identify and describe the
  magnitude of the injury problem, and to gain more insights (e.g. determine
  potential risk factors) by statistical modelling approaches. The 'injurytools'
  package provides standardized routines and utilities that simplify such
  analyses. It offers functions for data preparation, informative visualizations 
  and descriptive and model-based analyses.
	"""
	
	homepage = "https://github.com/lzumeta/injurytools"
	cran = "injurytools" 

	version("1.0.3", md5="f99f16912f346c91e635311fa4bc52e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
