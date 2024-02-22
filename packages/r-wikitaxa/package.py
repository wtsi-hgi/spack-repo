# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikitaxa(RPackage):
	"""Taxonomic Information from 'Wikipedia'

	'Taxonomic' information from 'Wikipedia', 'Wikicommons',
    'Wikispecies', and 'Wikidata'. Functions included for getting
    taxonomic information from each of the sources just listed, as
    well performing taxonomic search.
	"""
	
	homepage = "https://docs.ropensci.org/wikitaxa"
	cran = "wikitaxa" 

	version("0.4.0", md5="4fd3e9ef4b5ff5d10a908e8c742fd2fa")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-wikidatar", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-crul@0.3.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
