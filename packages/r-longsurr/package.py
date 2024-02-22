# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongsurr(RPackage):
	"""Longitudinal Surrogate Marker Analysis

	Assess the proportion of treatment effect explained by a longitudinal surrogate marker as described in Agniel D and Parast L (2021) <doi:10.1111/biom.13310>.
	"""
	
	cran = "longsurr" 

	version("1.0", md5="56cfa693df49384f5e575b581b0b4fe0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rsurrogate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
