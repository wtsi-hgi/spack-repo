# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbirdst(RPackage):
	"""Access and Analyze eBird Status and Trends Data Products

	Tools for accessing and analyzing eBird Status and
    Trends Data Products
    (<https://science.ebird.org/en/status-and-trends>). eBird
    (<https://ebird.org/home>) is a global database of bird observations
    collected by member of the public. eBird Status and Trends uses these
    data to model global bird distributions, abundances, and population trends 
    at a high spatial and temporal resolution.
	"""
	
	homepage = "https://ebird.github.io/ebirdst/"
	cran = "ebirdst" 

	version("3.2022.3", md5="a84a899ff4b845723fc6aa7a7d112acd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf@1.0.0:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra@1.6.3:", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
