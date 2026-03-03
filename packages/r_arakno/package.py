# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArakno(RPackage):
	"""ARAchnid KNowledge Online

	Allows the user to connect with the World Spider Catalogue (WSC; <https://wsc.nmbe.ch/>) and the World Spider Trait (WST; <https://spidertraits.sci.muni.cz/>) databases. Also performs several basic functions such as checking names validity, retrieving coordinate data from the Global Biodiversity Information Facility (GBIF; <https://www.gbif.org/>), and mapping.
	"""
	
	cran = "arakno" 

	version("1.3.0", md5="de4be9f71f1708d4861c6d36a601b323")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-rgbif", type=("build", "run"))
	depends_on("r-rworldmap", type=("build", "run"))
	depends_on("r-rworldxtra", type=("build", "run"))
