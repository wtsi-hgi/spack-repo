# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxadb(RPackage):
	"""A High-Performance Local Taxonomic Database Interface

	Creates a local database of many commonly used taxonomic authorities
             and provides functions that can quickly query this data.
	"""
	
	homepage = "<https://docs.ropensci.org/taxadb/>"
	cran = "taxadb" 

	version("0.2.1", md5="e0bc1e7f3669b4e10c373b92b721620b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-contentid", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
