# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebchem(RPackage):
	"""Chemical Information from the Web

	Chemical information from around the web. This package interacts 
    with a suite of web services for chemical information. Sources include: Alan
    Wood's Compendium of Pesticide Common Names, Chemical Identifier Resolver,
    ChEBI, Chemical Translation Service, ChemSpider, ETOX, Flavornet,
    NIST Chemistry WebBook, OPSIN, PubChem, SRS, Wikidata.
	"""
	
	homepage = "https://docs.ropensci.org/webchem/"
	cran = "webchem" 

	version("1.3.0", md5="d50a0dffdf77a744787a7b5eee0c7021")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
