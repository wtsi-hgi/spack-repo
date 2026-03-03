# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyitemanalysis(RPackage):
	"""Test and Item Analysis via Shiny

	Package including functions and interactive shiny application
    for the psychometric analysis of educational tests, psychological
    assessments, health-related and other types of multi-item
    measurements, or ratings from multiple raters.
	"""
	
	homepage = "http://www.ShinyItemAnalysis.org"
	cran = "ShinyItemAnalysis" 

	version("1.5.0", md5="ede75f1b53d13bce221703ec1c9a0b82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-difr@5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mirt@1.28:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-psych@2.1.9:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
