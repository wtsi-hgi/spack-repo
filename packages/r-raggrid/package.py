# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaggrid(RPackage):
	"""A Wrapper of the 'JavaScript' Library 'agGrid'

	Data objects in 'R' can be rendered as 'HTML' tables using the
    'JavaScript' library 'ag-grid' (typically via 'R Markdown' or 'Shiny'). The
    'ag-grid' library has been included in this 'R' package. The package name
    'RagGrid' is an abbreviation of 'R agGrid'.
	"""
	
	homepage = "https://github.com/no-types/RagGrid/"
	cran = "RagGrid" 

	version("0.2.0", md5="18a579936a29e3545f5fad78b4177cbe")

	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@1:", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
