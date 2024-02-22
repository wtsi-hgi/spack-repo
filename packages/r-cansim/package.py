# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCansim(RPackage):
	"""Accessing Statistics Canada Data Table and Vectors

	Searches for, accesses, and retrieves new-format and old-format Statistics Canada data 
    tables, as well as individual vectors, as tidy data frames. This package deals with encoding issues, allows for 
    bilingual English or French language data retrieval, and bundles convenience functions 
    to make it easier to work with retrieved table data. Optional caching features are provided.
	"""
	
	homepage = "https://github.com/mountainMath/cansim"
	cran = "cansim" 

	version("0.3.15", md5="0f4a10b34cc39214ed97e6a1fdec718f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-digest@0.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
