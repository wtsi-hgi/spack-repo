# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitationchaser(RPackage):
	"""Perform Forward and Backwards Chasing in Evidence Syntheses

	In searching for research articles, we often want to 
  obtain lists of references from across studies, and also obtain lists 
  of articles that cite a particular study. In systematic reviews, this 
  supplementary search technique is known as 'citation chasing': forward 
  citation chasing looks for all records citing one or more articles of 
  known relevance; backward citation chasing looks for all records 
  referenced in one or more articles. Traditionally, this process would 
  be done manually, and the resulting records would need to be checked 
  one-by-one against included studies in a review to identify potentially 
  relevant records that should be included in a review. This package 
  contains functions to automate this process by making use of the 
  Lens.org API. An input article list can be used to return a list of 
  all referenced records, and/or all citing records in the Lens.org 
  database (consisting of PubMed, PubMed Central, CrossRef, Microsoft 
  Academic Graph and CORE; <https://www.lens.org>). 
	"""
	
	cran = "citationchaser" 

	version("0.0.4", md5="4b81ecc36e32163d993166cc39ddb9d5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-maditr", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
