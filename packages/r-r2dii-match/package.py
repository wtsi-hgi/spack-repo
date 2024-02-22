# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2diiMatch(RPackage):
	"""Tools to Match Corporate Lending Portfolios with Climate Data

	These tools implement in R a fundamental part of the software
    'PACTA' (Paris Agreement Capital Transition Assessment), which is a
    free tool that calculates the alignment between financial portfolios
    and climate scenarios (<https://www.transitionmonitor.com/>). Financial
    institutions use 'PACTA' to study how their capital allocation
    decisions align with climate change mitigation goals. This package
    matches data from corporate lending portfolios to asset level data
    from market-intelligence databases (e.g. power plant capacities,
    emission factors, etc.). This is the first step to assess if a
    financial portfolio aligns with climate goals.
	"""
	
	homepage = "https://rmi-pacta.github.io/r2dii.match/"
	cran = "r2dii.match" 

	version("0.1.4", md5="51d6b5a6abb77d200fbebb2439057a8c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r2dii-data@0.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
