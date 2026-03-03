# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackagefinder(RPackage):
	"""Comfortable Search for R Packages on CRAN, Either Directly from
the R Console or with an R Studio Add-in

	Search for R packages on CRAN directly from the R console, based on the packages' titles, short and long descriptions, or other fields. Combine multiple keywords with logical operators ('and', 'or'), view detailed information on any package and keep track of the latest package contributions to CRAN. If you don't want to search from the R console, use the comfortable R Studio add-in.
	"""
	
	homepage = "https://github.com/jsugarelli/packagefinder/"
	cran = "packagefinder" 

	version("0.3.5", md5="c873cd60c868bea9c6aeeb609f6a773f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
	depends_on("r-htmltable", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
