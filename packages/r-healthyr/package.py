# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyr(RPackage):
	"""Hospital Data Analysis Workflow Tools

	
    Hospital data analysis workflow tools, modeling, and automations. This library
    provides many useful tools to review common administrative hospital data. Some 
    of these include average length of stay, readmission rates, average net pay
    amounts by service lines just to name a few. The aim is to provide a simple
    and consistent verb framework that takes the guesswork out of everything.
	"""
	
	homepage = "https://github.com/spsanderson/healthyR"
	cran = "healthyR" 

	version("0.2.1", md5="56954ea811c043ab7a8f949aac17318c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-timetk", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
