# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtasr(RPackage):
	"""Functions to Replicate the Center for Disease Control and
Prevention's 'LTAS' Software in R

	A suite of functions for reading in a rate file in XML format, 
    stratify a cohort, and calculate 'SMRs' from the stratified cohort and rate file. 
	"""
	
	cran = "LTASR" 

	version("0.1.2", md5="727fdcd70e3d18ed1964460105f309f9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
