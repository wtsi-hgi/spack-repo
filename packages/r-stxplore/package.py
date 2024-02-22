# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStxplore(RPackage):
	"""Exploration of Spatio-Temporal Data

	A set of statistical tools for spatio-temporal data exploration.     
    Includes simple plotting functions, covariance calculations and computations 
    similar to principal component analysis for spatio-temporal data. Can use 
    both dataframes and stars objects for all plots and computations. For more 
    details refer 'Spatio-Temporal Statistics with R' (Christopher K. Wikle, 
    Andrew Zammit-Mangion, Noel Cressie, 2019, ISBN:9781138711136).
	"""
	
	homepage = "https://sevvandi.github.io/stxplore/"
	cran = "stxplore" 

	version("0.1.0", md5="923773ecdc238e93eb5386b03e4f4caf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
