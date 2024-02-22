# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScipub(RPackage):
	"""Summarize Data for Scientific Publication

	Create and format tables and APA statistics for
    scientific publication. This includes making a 'Table 1'
    to summarize demographics across groups, correlation tables
    with significance indicated by stars, and extracting formatted
    statistical summarizes from simple tests for in-text notation.
    The package also includes functions for Winsorizing data based
    on a Z-statistic cutoff.  
	"""
	
	homepage = "https://github.com/dpagliaccio/scipub"
	cran = "scipub" 

	version("1.2.2", md5="73f04d16036ca1aac41f965e68f4a0bb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gghalves", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
