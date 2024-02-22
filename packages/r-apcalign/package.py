# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcalign(RPackage):
	"""Resolving Plant Taxon Names Using the Australian Plant Census

	The process of resolving taxon names is necessary when working with biodiversity data. 'APCalign' uses the Australian Plant Census (APC) and the Australian Plant Name Index (APNI) to align and update plant taxon names to current, accepted standards. 'APCalign' also supplies information about the established status of plant taxa across different states/territories.
	"""
	
	homepage = "https://traitecoevo.github.io/APCalign/"
	cran = "APCalign" 

	version("0.1.3", md5="3378aa0ebf19d24eaa58077e0e32b0a1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
