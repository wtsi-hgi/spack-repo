# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuxtable(RPackage):
	"""Easily Create and Style Tables for LaTeX, HTML and Other Formats

	Creates styled tables for data presentation. Export to HTML, LaTeX,
  RTF, 'Word', 'Excel', and 'PowerPoint'. Simple, modern interface to manipulate 
  borders, size, position, captions, colours, text styles and number formatting.
  Table cells can span multiple rows and/or columns.
  Includes  a 'huxreg' function for creation of regression tables, and 'quick_*' 
  one-liners to print data to a new document.
	"""
	
	homepage = "https://hughjonesd.github.io/huxtable/"
	cran = "huxtable" 

	version("5.5.6", md5="3a41ec32c695d2dc08f2ad4a6849f9dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
