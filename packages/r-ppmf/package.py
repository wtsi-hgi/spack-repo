# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpmf(RPackage):
	"""Read Census Privacy Protected Microdata Files

	Implements data processing described in <doi:10.1126/sciadv.abk3283> to align modern differentially private data with formatting of older US Census data releases. The primary goal is to read in Census Privacy Protected Microdata Files data in a reproducible way. This includes tools for aggregating to relevant levels of geography by creating geographic identifiers which match the US Census Bureau's numbering. Additionally, there are tools for grouping race numeric identifiers into categories, consistent with OMB (Office of Management and Budget) classifications. Functions exist for downloading and linking to existing sources of privacy protected microdata.
	"""
	
	homepage = "https://github.com/christopherkenny/ppmf/"
	cran = "ppmf" 

	version("0.1.3", md5="7bd4b2a6d5ed8c4f997594bb15e7b72d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-censable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
