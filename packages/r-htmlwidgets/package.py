# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmlwidgets(RPackage):
	"""HTML Widgets for R.

	A framework for creating HTML widgets that render in various contexts
	including the R console, 'R Markdown' documents, and 'Shiny' web
	applications."""

	cran = "htmlwidgets"

	license("MIT")

	version("1.6.4", md5="e1ea7f9774ad7a79fcf31e52c2074fd1")

	depends_on("r-htmltools@0.5.7:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-knitr@1.8:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
