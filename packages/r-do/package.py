# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDo(RPackage):
	"""Data Operator

	Flexibly convert data between long and wide format using just two
    functions: reshape_toLong() and reshape_toWide().
	"""
	
	homepage = "https://github.com/yikeshu0611/do"
	cran = "do" 

	version("2.0.0.0", md5="f89af897b6b03444fdfa63d91d51ef0a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tmcn", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
