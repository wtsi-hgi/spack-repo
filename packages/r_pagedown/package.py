# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagedown(RPackage):
	"""Paginate the HTML Output of R Markdown with CSS for Print

	Use the paged media properties in CSS and the JavaScript
  library 'paged.js' to split the content of an HTML document into discrete
  pages. Each page can have its page size, page numbers, margin boxes, and
  running headers, etc. Applications of this package include books, letters,
  reports, papers, business cards, resumes, and posters.
	"""
	
	homepage = "https://github.com/rstudio/pagedown"
	cran = "pagedown" 

	version("0.20", md5="5c0eb2ea9a3c55ab133fcff2d65a4a8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown@2.13:", type=("build", "run"))
	depends_on("r-bookdown@0.8:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-later@1:", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-servr@0.23:", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-websocket", type=("build", "run"))
	depends_on("pandoc@2.2.3:", type=("build", "link", "run"))
