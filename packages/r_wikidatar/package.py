# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikidatar(RPackage):
	"""Read-Write API Client Library for Wikidata

	Read from, interogate, and write to Wikidata <https://www.wikidata.org> -
    the multilingual, interdisciplinary, semantic knowledgebase. Includes functions to:
    read from wikidata (single items, properties, or properties); query wikidata (retrieving
    all items that match a set of criterial via Wikidata SPARQL query service); write to
    Wikidata (adding new items or statements via QuickStatements); and handle and manipulate
    Wikidata objects (as lists and tibbles). Uses the Wikidata and Quickstatements APIs. 
	"""
	
	homepage = "https://github.com/TS404/WikidataR"
	cran = "WikidataR" 

	version("2.3.3", md5="a77491c480fdee39a14f2e3feafc4780")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-wikipedir", type=("build", "run"))
	depends_on("r-wikidataqueryservicer", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
