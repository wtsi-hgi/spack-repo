# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobis(RPackage):
	"""Ocean Biodiversity Information System (OBIS) Client

	Client for the Ocean Biodiversity Information System (<https://obis.org>).
	"""
	
	homepage = "https://github.com/iobis/robis"
	cran = "robis" 

	version("2.11.3", md5="1b9e3cb5689c0709c4a0bd2d85e2481f")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-httpcache", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mapedit", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
