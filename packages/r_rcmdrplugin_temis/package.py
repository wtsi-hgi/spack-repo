# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginTemis(RPackage):
	"""Graphical Integrated Text Mining Solution

	An 'R Commander' plug-in providing an integrated solution to perform
    a series of text mining tasks such as importing and cleaning a corpus, and
    analyses like terms and documents counts, vocabulary tables, terms
    co-occurrences and documents similarity measures, time series analysis,
    correspondence analysis and hierarchical clustering. Corpora can be imported
    from spreadsheet-like files, directories of raw text files, 'Twitter' queries,
    as well as from 'Dow Jones Factiva', 'LexisNexis', 'Europresse' and 'Alceste' files.
	"""
	
	homepage = "https://github.com/nalimilan/R.TeMiS"
	cran = "RcmdrPlugin.temis" 

	version("0.7.10", md5="59668af2abe71e7bec60121af98c1736")

	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcmdr@2.1.1:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-ca", type=("build", "run"))
	depends_on("r-r2html@2.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
