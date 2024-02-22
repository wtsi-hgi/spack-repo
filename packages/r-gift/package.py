# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGift(RPackage):
	"""Access to the Global Inventory of Floras and Traits (GIFT)

	Retrieving regional plant checklists, species traits and
  distributions, and environmental data from the Global Inventory of Floras and
  Traits (GIFT). More information about the GIFT database can be found at
  <https://gift.uni-goettingen.de/about> and the map of available floras can be
  visualized at <https://gift.uni-goettingen.de/map>. The API and associated
  queries can be accessed according the following scheme:
  <https://gift.uni-goettingen.de/api/extended/index2.0.php?query=env_raster>.
	"""
	
	homepage = "https://github.com/BioGeoMacro/GIFT"
	cran = "GIFT" 

	version("1.3.1", md5="251cf9e9b69e591b7e17b2d83a22043b")

	depends_on("r@3.5.3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
