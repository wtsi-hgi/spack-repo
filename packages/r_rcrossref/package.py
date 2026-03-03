# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcrossref(RPackage):
	"""Client for Various 'CrossRef' 'APIs'

	Client for various 'CrossRef' 'APIs', including 'metadata' search
    with their old and newer search 'APIs', get 'citations' in various formats
    (including 'bibtex', 'citeproc-json', 'rdf-xml', etc.), convert 'DOIs'
    to 'PMIDs', and 'vice versa', get citations for 'DOIs', and get links to
    full text of articles when available.
	"""
	
	homepage = "https://docs.ropensci.org/rcrossref/"
	cran = "rcrossref" 

	version("1.2.0", md5="088dca570f041e1977404653de7d6fdb")

	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-crul@0.7.4:", type=("build", "run"))
	depends_on("r-xml2@1.1.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
