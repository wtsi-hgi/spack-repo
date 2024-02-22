# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRusda(RPackage):
	"""Interface to USDA Databases

	An interface to the web service methods provided by the United States Department of Agriculture (USDA). The Agricultural Research Service (ARS) provides a large set of databases. The current version of the package holds interfaces to the Systematic Mycology and Microbiology Laboratory (SMML), which consists of four databases: Fungus-Host Distributions, Specimens, Literature and the Nomenclature database. It provides functions for querying these databases. The main function is code{associations}, which allows searching for fungus-host combinations. 
	"""
	
	homepage = "http://www.usda.gov/wps/portal/usda/usdahome"
	cran = "rusda" 

	version("1.0.8", md5="733e39e081bf842b9ac00a1aa1a031b1")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
