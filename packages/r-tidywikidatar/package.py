# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidywikidatar(RPackage):
	"""Explore 'Wikidata' Through Tidy Data Frames

	Query 'Wikidata' API <https://www.wikidata.org/wiki/Wikidata:Main_Page> with ease, get tidy data frames in response, and cache data in a local database.
	"""
	
	homepage = "https://edjnet.github.io/tidywikidatar/"
	cran = "tidywikidatar" 

	version("0.5.8", md5="0bc74d70983c8e09775821c6da60c667")
	version("0.5.7", md5="2cc59aec4377e97d7608b1b3ce52de96")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-wikidatar", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-wikidataqueryservicer", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pool", type=("build", "run"))
	depends_on("r-wikipedir", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
