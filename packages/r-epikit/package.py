# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpikit(RPackage):
	"""Miscellaneous Helper Tools for Epidemiologists

	Contains tools for formatting inline code, renaming redundant
  columns, aggregating age categories, adding survey weights, finding the earliest
  date of an event, plotting z-curves, generating population counts and 
  calculating proportions with confidence intervals. This is part of the 
  'R4Epis' project <https://r4epis.netlify.app/>.
	"""
	
	homepage = "https://github.com/R4EPI/epikit"
	cran = "epikit" 

	version("0.1.6", md5="fb61e2caafd623dc4e1a875846fd0530")

	depends_on("r-binom", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
