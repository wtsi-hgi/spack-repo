# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTippy(RPackage):
	"""Add Tooltips to 'R markdown' Documents or 'Shiny' Apps

	'Htmlwidget' of 'Tippyjs' to add tooltips to 'Shiny' apps and 'R markdown' documents.
	"""
	
	homepage = "https://tippy.john-coene.com/"
	cran = "tippy" 

	version("0.1.0", md5="1ae95fcb4ee257e4fb56db8d45ede216")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
