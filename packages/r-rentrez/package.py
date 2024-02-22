# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRentrez(RPackage):
	"""'Entrez' in R

	Provides an R interface to the NCBI's 'EUtils' API, 
    allowing users to search databases like 'GenBank' 
    <https://www.ncbi.nlm.nih.gov/genbank/> and 'PubMed' 
    <https://pubmed.ncbi.nlm.nih.gov/>, process the 
    results of those searches and pull data into their R sessions.
	"""
	
	homepage = "https://docs.ropensci.org/rentrez/"
	cran = "rentrez" 

	version("1.2.3", md5="729cb748ac72fbdddce5b719dae803c6")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr@0.5:", type=("build", "run"))
	depends_on("r-jsonlite@0.9:", type=("build", "run"))
