# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmltable(RPackage):
	"""Advanced Tables for Markdown/HTML.

	Tables with state-of-the-art layout elements such as row spanners, column
	spanners, table spanners, zebra striping, and more. While allowing advanced
	layout, the underlying css-structure is simple in order to maximize
	compatibility with word processors such as 'MS Word' or 'LibreOffice'. The
	package also contains a few text formatting functions that help outputting
	text compatible with HTML/'LaTeX'."""

	cran = "htmlTable"

	version("2.4.2", md5="7f7e17fb6c8b39a0ac8312566f44a17a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-knitr@1.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rstudioapi@0.6:", type=("build", "run"))
