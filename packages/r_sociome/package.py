# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSociome(RPackage):
	"""Operationalizing Social Determinants of Health Data for
Researchers

	Accesses raw data via API and calculates social
    determinants of health measures for user-specified locations in the
    US, returning them in tidyverse- and sf-compatible data frames.
	"""
	
	cran = "sociome" 

	version("2.2.5", md5="42a59b1aa3906362755cd560bb1f025c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mice@3.10.0.1:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidycensus@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
