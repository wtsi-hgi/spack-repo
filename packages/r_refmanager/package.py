# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefmanager(RPackage):
	"""Straightforward 'BibTeX' and 'BibLaTeX' Bibliography Management

	Provides tools for importing and working with bibliographic
    references. It greatly enhances the 'bibentry' class by providing a class
    'BibEntry' which stores 'BibTeX' and 'BibLaTeX' references, supports 'UTF-8'
    encoding, and can be easily searched by any field, by date ranges, and by
    various formats for name lists (author by last names, translator by full names,
    etc.). Entries can be updated, combined, sorted, printed in a number of styles,
    and exported. 'BibTeX' and 'BibLaTeX' '.bib' files can be read into 'R' and
    converted to 'BibEntry' objects. Interfaces to 'NCBI Entrez', 'CrossRef', and
    'Zotero' are provided for importing references and references can be created
    from locally stored 'PDF' files using 'Poppler'. Includes functions for citing
    and generating a bibliography with hyperlinks for documents prepared with
    'RMarkdown' or 'RHTML'.
	"""
	
	homepage = "https://github.com/ropensci/RefManageR/"
	cran = "RefManageR" 

	version("1.4.0", md5="0548595d653bf6a1e406f9d6833d85e4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate@1.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bibtex@0.4.1:", type=("build", "run"))
