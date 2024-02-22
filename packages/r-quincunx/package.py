# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuincunx(RPackage):
	"""REST API Client for the 'PGS' Catalog

	Programmatic access to the 'PGS' Catalog.
    This package provides easy access to 'PGS' Catalog data by
    accessing the REST API <https://www.pgscatalog.org/rest/>.
	"""
	
	homepage = "https://github.com/ramiromagno/quincunx"
	cran = "quincunx" 

	version("0.1.7", md5="a087fcb79befa241de9f8f1707364280")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyjson", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-concatenate", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
