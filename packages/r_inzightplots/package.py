# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInzightplots(RPackage):
	"""Graphical Tools for Exploring Data with 'iNZight'

	Simple plotting function(s) for exploratory data analysis with flexible options allowing for easy plot customisation. The goal is to make it easy for beginners to start exploring a dataset through simple R function calls, as well as provide a similar interface to summary statistics and inference information. Includes functionality to generate interactive HTML-driven graphs. Used by 'iNZight', a graphical user interface providing easy exploration and visualisation of data for students of statistics, available in both desktop and online versions.
	"""
	
	homepage = "https://inzight.nz"
	cran = "iNZightPlots" 

	version("2.15.3", md5="c4740a9a7de1b56e2353a24d3f7e0903")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dichromat", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-expss", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-inzightmr@2.2.7:", type=("build", "run"))
	depends_on("r-inzighttools@1.9:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s20x", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
