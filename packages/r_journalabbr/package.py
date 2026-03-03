# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJournalabbr(RPackage):
	"""Journal Abbreviations for BibTeX Documents

	Since the reference management software (such as 'Zotero', 'Mendeley') exports Bib file journal abbreviation is not detailed enough, the 'journalabbr' package only abbreviates the journal field of Bib file, and then outputs a new Bib file for generating reference format with journal abbreviation on other software (such as 'texstudio'). The abbreviation table is from 'JabRef'. At the same time, 'Shiny' application is provided to generate 'thebibliography', a reference format that can be directly used for latex paper writing based on 'Rmd' files.
	"""
	
	homepage = "https://github.com/zoushucai/journalabbr"
	cran = "journalabbr" 

	version("0.4.3", md5="0e6a77c5435e22a9cae259acc88c772c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-tidytable@0.11:", type=("build", "run"))
	depends_on("r-stringi@1.7:", type=("build", "run"))
