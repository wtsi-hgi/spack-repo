# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpidr(RPackage):
	"""Spider Knowledge Online

	Allows the user to connect with the World Spider Catalogue (WSC; <https://wsc.nmbe.ch/>) and the World Spider Trait (WST; <https://spidertraits.sci.muni.cz/>) databases. Also performs several basic functions such as checking names validity, retrieving coordinate data from the Global Biodiversity Information Facility (GBIF; <https://www.gbif.org/>), and mapping.
	"""
	
	cran = "spidR" 

	version("1.0.2", md5="7d729e8902016b5b31302b68ebc09955")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rgbif", type=("build", "run"))
	depends_on("r-rworldmap", type=("build", "run"))
	depends_on("r-rworldxtra", type=("build", "run"))
