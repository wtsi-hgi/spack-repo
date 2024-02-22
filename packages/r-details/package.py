# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetails(RPackage):
	"""Create Details HTML Tag for Markdown and Package Documentation

	Create a details HTML tag around R objects to place
    in a Markdown, 'Rmarkdown' and 'roxygen2' documentation.
	"""
	
	homepage = "https://github.com/yonicd/details"
	cran = "details" 

	version("0.3.0", md5="e8c0d6c401fe4d813300e0b45322d3bc")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
