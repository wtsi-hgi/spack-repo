# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablehtml(RPackage):
	"""A Tool to Create HTML Tables

	A tool to create and style HTML tables with CSS. These can
    be exported and used in any application that accepts HTML (e.g. 'shiny',
    'rmarkdown', 'PowerPoint'). It also provides functions to create CSS files
    (which also work with shiny).
	"""
	
	homepage = "https://github.com/LyzandeR/tableHTML"
	cran = "tableHTML" 

	version("2.1.2", md5="662ae3697eff7719a28363857f98dd07")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
