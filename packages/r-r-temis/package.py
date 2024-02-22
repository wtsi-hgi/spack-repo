# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRTemis(RPackage):
	"""Integrated Text Mining Solution

	An integrated solution to perform
    a series of text mining tasks such as importing and cleaning a corpus, and
    analyses like terms and documents counts, lexical summary, terms
    co-occurrences and documents similarity measures, graphs of terms,
    correspondence analysis and hierarchical clustering. Corpora can be imported
    from spreadsheet-like files, directories of raw text files,
    as well as from 'Dow Jones Factiva', 'LexisNexis', 'Europresse' and 'Alceste' files.
	"""
	
	homepage = "https://github.com/nalimilan/R.TeMiS"
	cran = "R.temis" 

	version("0.1.3", md5="c217f447ae6994463b5e24554cef17e3")

	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-explor", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-tm-plugin-factiva", type=("build", "run"))
	depends_on("r-tm-plugin-lexisnexis", type=("build", "run"))
	depends_on("r-tm-plugin-europresse", type=("build", "run"))
	depends_on("r-tm-plugin-alceste", type=("build", "run"))
