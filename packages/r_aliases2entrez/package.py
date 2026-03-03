# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAliases2entrez(RPackage):
	"""Converts Human gene symbols to entrez IDs

	Queries multiple resources authors HGNC (2019) <https://www.genenames.org>, authors limma (2015) <doi:10.1093/nar/gkv007> 
    to find the correspondence between evolving nomenclature of human gene symbols, aliases, previous symbols or synonyms with 
    stable, curated gene entrezID from NCBI database. This allows fast, accurate and up-to-date correspondence
    between human gene expression datasets from various date and platform (e.g: gene symbol: BRCA1 - ID: 672).
	"""
	
	cran = "aliases2entrez" 

	version("0.1.2", md5="04f00714a85ae92f82a61deacf288f57")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
