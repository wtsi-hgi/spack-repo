# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJbrowser(RPackage):
	"""An R Interface to the JBrowse 2 Genome Browser

	Provides an R interface to the JBrowse 2 genome browser.
    Enables embedding a JB2 genome browser in a Shiny app or R Markdown
    document. The browser can also be launched from an interactive R console.
    The browser can be loaded with a variety of common genomics data types,
    and can be used with a custom theme.
	"""
	
	homepage = "https://gmod.github.io/JBrowseR/"
	cran = "JBrowseR" 

	version("0.10.2", md5="9fa31e312e491f4855f16b0bf8d2abc8")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ids", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
