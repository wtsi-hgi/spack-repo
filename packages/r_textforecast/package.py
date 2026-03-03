# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextforecast(RPackage):
	"""Regression Analysis and Forecasting Using Textual Data from a
Time-Varying Dictionary

	Provides functionalities based on the paper "Time Varying Dictionary and the Predictive Power of FED Minutes" (Lima, 2018) <doi:10.2139/ssrn.3312483>. It selects the most predictive terms, that we call time-varying dictionary using supervised machine learning techniques as lasso and elastic net.     
	"""
	
	homepage = "https://github.com/lucasgodeiro/TextForecast"
	cran = "TextForecast" 

	version("0.1.3", md5="75344dc3f6c4f20f78fc4f04f9a73615")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-udpipe", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
