# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleants(RPackage):
	"""Testbench for Univariate Time Series Cleaning

	A reliable and efficient tool for cleaning univariate time 
    series data. It implements reliable and efficient procedures for 
    automating the process of cleaning univariate time series data. 
    The package provides integration with already developed and deployed 
    tools for missing value imputation and outlier detection. It also 
    provides a way of visualizing large time-series data in different 
    resolutions.
	"""
	
	homepage = "https://github.com/Mayur1009/cleanTS"
	cran = "cleanTS" 

	version("0.1.2", md5="b8be6b7544705fe0fc8eacb960e649a6")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-transformr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-imputetestbench", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
