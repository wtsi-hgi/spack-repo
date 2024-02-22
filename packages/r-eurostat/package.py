# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REurostat(RPackage):
	"""Tools for Eurostat Open Data

	Tools to download data from the Eurostat database
    <https://ec.europa.eu/eurostat> together with search and manipulation
    utilities.
	"""
	
	homepage = "https://ropengov.github.io/eurostat/"
	cran = "eurostat" 

	version("4.0.0", md5="09cbd06dc215f033c063c09350244ce9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2@0.2.3:", type=("build", "run"))
	depends_on("r-isoweek", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-refmanager", type=("build", "run"))
	depends_on("r-regions", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
