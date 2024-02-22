# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REurodata(RPackage):
	"""Fast and Easy Eurostat Data Import and Search

	Interface to Eurostat’s API (SDMX 2.1) with fast data.table-based import of
    data, labels, and metadata. On top of the core functionality, data search and data
    description/comparison functions are also provided.
    Use <https://github.com/alekrutkowski/eurodata_codegen> — a point-and-click app for rapid and
    easy generation of richly-commented R code — to import a Eurostat dataset or its subset
    (based on the eurodata::importData() function).
	"""
	
	homepage = "https://github.com/alekrutkowski/eurodata/"
	cran = "eurodata" 

	version("1.7.0", md5="c130bf172cdb96abd9a3771a5910958b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
