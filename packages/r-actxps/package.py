# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActxps(RPackage):
	"""Create Actuarial Experience Studies: Prepare Data, Summarize
Results, and Create Reports

	Experience studies are used by actuaries to explore historical
    experience across blocks of business and to inform assumption setting
    activities. This package provides functions for preparing data, creating 
    studies, visualizing results, and beginning assumption development. 
    Experience study methods, including exposure calculations, are described in:
    Atkinson & McGarry (2016) "Experience Study Calculations" 
    <https://www.soa.org/49378a/globalassets/assets/files/research/experience-study-calculations.pdf>.
    The limited fluctuation credibility method used by the 'exp_stats()'
    function is described in: Herzog (1999, ISBN:1-56698-374-6) 
    "Introduction to Credibility Theory".
	"""
	
	homepage = "https://github.com/mattheaphy/actxps/"
	cran = "actxps" 

	version("1.4.0", md5="60f531129bf662adaaa762d9d3843803")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gt@0.9:", type=("build", "run"))
	depends_on("r-paletteer", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
