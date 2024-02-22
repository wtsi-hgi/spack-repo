# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidata(RPackage):
	"""Validate Data Frames

	Functions for validating the structure and properties of data frames. Answers essential questions about a data set after initial import or modification. What are the unique or missing values? What columns form a primary key? What are the properties of the numeric or categorical columns? What kind of overlap or mapping exists between 2 columns?
	"""
	
	homepage = "https://harrison4192.github.io/validata/"
	cran = "validata" 

	version("0.1.0", md5="48cd4a548e190a480b4bf0fdd3a691bb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-listviewer", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-framecleaner", type=("build", "run"))
	depends_on("r-badger", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
