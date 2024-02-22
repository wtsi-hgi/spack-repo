# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConflr(RPackage):
	"""Client for 'Confluence' API

	Provides utilities for working with various 'Confluence' API 
    <https://docs.atlassian.com/ConfluenceServer/rest/latest/>, including a
    functionality to convert an R Markdown document to 'Confluence' format and
    upload it to 'Confluence' automatically.
	"""
	
	homepage = "https://line.github.io/conflr/"
	cran = "conflr" 

	version("0.1.1", md5="b0390a0045d2bca9bec66a22514394ed")

	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
