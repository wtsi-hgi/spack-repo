# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIheiddown(RPackage):
	"""For Writing Geneva Graduate Institute Documents

	A set of tools for writing documents
    according to Geneva Graduate Institute conventions and regulations.
    The most common use is for writing and compiling theses or thesis
    chapters, as drafts or for examination with correct preamble formatting. 
    However, the package also offers users to create HTML presentation
    slides with 'xaringan', complete problem sets, format posters, and, 
    for course instructors, prepare a syllabus.
    The package includes additional functions for institutional color palettes,
    an institutional 'ggplot' theme, a function for counting manuscript words,
    and a bibliographical analysis toolkit.
	"""
	
	homepage = "https://github.com/jhollway/iheiddown"
	cran = "iheiddown" 

	version("0.9.7", md5="3431c8cc72f9fbedaffbcbd4aff35271")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-xaringan", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-bib2df", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-gender", type=("build", "run"))
	depends_on("r-pagedown", type=("build", "run"))
