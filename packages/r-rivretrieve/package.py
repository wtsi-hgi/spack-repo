# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRivretrieve(RPackage):
	"""Retrieve Global River Gauge Data

	Provides access to global river gauge data from a variety of national-level river agencies. The package interfaces with the national-level agency websites to provide access to river gauge locations, river discharge, and river stage. Currently, the package is available for the following countries: Australia, Brazil, Canada, Chile, France, Japan, South Africa, the United Kingdom, and the United States.
	"""
	
	homepage = "https://github.com/Ryan-Riggs/RivRetrieve"
	cran = "RivRetrieve" 

	version("0.1.4", md5="694ed6e12b2397b5fd47a26054195b34")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-dataretrieval", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyhydat", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
