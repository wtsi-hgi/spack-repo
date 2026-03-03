# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPestr(RPackage):
	"""Interface to Download Data on Pests and Hosts from 'EPPO'

	Set of tools to automatize extraction of data on pests from 'EPPO
    Data Services' and 'EPPO Global Database' and to put them into tables with
    human readable format. Those function use 'EPPO database API', thus you 
    first need to register on <https://data.eppo.int> (free of charge).
    Additional helpers allow to download, check and connect to
    'SQLite EPPO database'.
	"""
	
	homepage = "https://github.com/mczyzj/pestr"
	cran = "pestr" 

	version("0.8.2", md5="68fd11b9f6d34201e8fd072e3139aaf2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
