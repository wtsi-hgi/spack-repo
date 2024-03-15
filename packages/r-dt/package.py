# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDt(RPackage):
	"""A Wrapper of the JavaScript Library 'DataTables'.

	Data objects in R can be rendered as HTML tables using the JavaScript
	library 'DataTables' (typically via R Markdown or Shiny). The 'DataTables'
	library has been included in this R package. The package name 'DT' is an
	abbreviation of 'DataTables'."""

	cran = "DT"

	license("Apache-2.0")

	version("0.32", md5="e43c80e1b807de68609808b62971034c")

	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.3:", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
