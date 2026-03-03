# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxize(RPackage):
	"""Taxonomic Information from Around the Web

	Interacts with a suite of web 'APIs' for taxonomic tasks,
    such as getting database specific taxonomic identifiers, verifying
    species names, getting taxonomic hierarchies, fetching downstream and
    upstream taxonomic names, getting taxonomic synonyms, converting
    scientific to common names and vice versa, and more.
	"""
	
	homepage = "https://docs.ropensci.org/taxize/"
	cran = "taxize" 

	version("0.9.100", md5="9f942dbb5859b335061806a4185c439a")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-crul@0.7:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-bold@0.8.6:", type=("build", "run"))
	depends_on("r-rredlist", type=("build", "run"))
	depends_on("r-rotl@3:", type=("build", "run"))
	depends_on("r-ritis@0.7.6:", type=("build", "run"))
	depends_on("r-worrms@0.4:", type=("build", "run"))
	depends_on("r-natserv@1:", type=("build", "run"))
	depends_on("r-wikitaxa@0.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-conditionz", type=("build", "run"))
