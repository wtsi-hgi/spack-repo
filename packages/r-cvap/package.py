# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvap(RPackage):
	"""Citizen Voting Age Population

	Works with the Citizen Voting Age Population special tabulation from the US Census Bureau <https://www.census.gov/programs-surveys/decennial-census/about/voting-rights/cvap.html>. Provides tools to download and process raw data. Also provides a downloading interface to processed data. Implements a very basic approach to estimate block level citizen voting age population from block group data.
	"""
	
	homepage = "https://github.com/christopherkenny/cvap"
	cran = "cvap" 

	version("0.1.4", md5="65c7278aa792cb27424441145c4601f6")
	version("0.1.5", md5="aad36adc9f96b3fa798b71b71ade591c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-censable", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
