# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInzightregression(RPackage):
	"""Tools for Exploring Regression Models with 'iNZight'

	Provides a suite of functions to use with regression models, including summaries, residual plots, and factor comparisons. Used as part of the Model Fitting module of 'iNZight', a graphical user interface providing easy exploration and visualisation of data for students of statistics, available in both desktop and online versions.
	"""
	
	homepage = "https://inzight.nz"
	cran = "iNZightRegression" 

	version("1.3.3", md5="e361b734015a61f8230658517bd73b37")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-inzightplots@2.13:", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
