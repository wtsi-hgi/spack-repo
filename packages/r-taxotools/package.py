# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxotools(RPackage):
	"""Taxonomic List Processing

	Taxonomic lists matching and merging, casting and melting 
  scientific names, managing taxonomic lists from  Global Biodiversity 
  Information Facility 'GBIF' or Integrated Taxonomic Information System 'ITIS',
  harvesting names from Wikipedia and fuzzy matching.
	"""
	
	cran = "taxotools" 

	version("0.0.132", md5="a3c56627f1d5a30a5096629b70ae8b24")

	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-wikitaxa", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
