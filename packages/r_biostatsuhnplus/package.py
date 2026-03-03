# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiostatsuhnplus(RPackage):
	"""Nested Data Summary and Adverse Events

	Miscellaneous code snippets and functions with pipes and
    multiple package dependencies used for summarizing nested data and 
    adverse events.
	"""
	
	cran = "BiostatsUHNplus" 

	version("0.0.9", md5="fa81d756ce157bbaaca8de21e307b05e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-afex", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reportrmd", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
