# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunmodeling(RPackage):
	"""Exploratory Data Analysis and Data Preparation Tool-Box

	Around 10% of almost any predictive modeling project is spent in predictive modeling, 'funModeling' and the book Data Science Live Book (<https://livebook.datascienceheroes.com/>) are intended to cover remaining 90%: data preparation, profiling, selecting best variables 'dataViz', assessing model performance and other functions.
	"""
	
	homepage = "https://livebook.datascienceheroes.com"
	cran = "funModeling" 

	version("1.9.5", md5="7ccfe01086ad4b59b60e076db9efce62")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-hmisc@3.17.1:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
