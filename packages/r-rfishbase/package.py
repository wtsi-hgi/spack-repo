# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfishbase(RPackage):
	"""R Interface to 'FishBase'

	A programmatic interface to 'FishBase', re-written
    based on an accompanying 'RESTful' API. Access tables describing over 30,000
    species of fish, their biology, ecology, morphology, and more. This package also
    supports experimental access to 'SeaLifeBase' data, which contains
    nearly 200,000 species records for all types of aquatic life not covered by
    'FishBase.'
	"""
	
	homepage = "https://docs.ropensci.org/rfishbase/"
	cran = "rfishbase" 

	version("4.1.2", md5="1c6f1ed62eab3b17ec3d9d3579839895")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-contentid@0.0.15:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
