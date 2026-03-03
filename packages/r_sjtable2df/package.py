# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSjtable2df(RPackage):
	"""Convert 'sjPlot' HTML-Tables to R 'data.frame'

	A small set of helper functions to convert 'sjPlot'
    HTML-tables to R data.frame objects / knitr::kable-tables.
	"""
	
	homepage = "https://github.com/kapsner/sjtable2df"
	cran = "sjtable2df" 

	version("0.0.3", md5="c2962f96012ed27214b3b0e24fd66d1b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
