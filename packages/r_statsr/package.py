# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatsr(RPackage):
	"""Companion Software for the Coursera Statistics with R
Specialization

	Data and functions to support Bayesian and frequentist inference and decision making 
            for the Coursera Specialization "Statistics with R".
            See <https://github.com/StatsWithR/statsr> for more information.
	"""
	
	homepage = "https://github.com/StatsWithR/statsr"
	cran = "statsr" 

	version("0.3.0", md5="33feaa8820da9fcba58c468bca0c73d6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
