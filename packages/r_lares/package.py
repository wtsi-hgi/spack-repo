# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLares(RPackage):
	"""Analytics & Machine Learning Sidekick

	Auxiliary package for better/faster analytics, visualization, data mining, and machine
    learning tasks. With a wide variety of family functions, like Machine Learning, Data Wrangling,
    Exploratory, API, and Scrapper, it helps the analyst or data scientist to get quick and robust
    results, without the need of repetitive coding or extensive R programming skills.
	"""
	
	homepage = "https://github.com/laresbernardo/lares"
	cran = "lares" 

	version("5.2.5", md5="d9133d20d731feb208b1d7d42ed4b5f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
