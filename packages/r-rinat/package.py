# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRinat(RPackage):
	"""Access 'iNaturalist' Data Through APIs

	A programmatic interface to the API provided by the 'iNaturalist' website <https://www.inaturalist.org/> to download species occurrence data submitted by citizen scientists.
	"""
	
	homepage = "https://docs.ropensci.org/rinat/"
	cran = "rinat" 

	version("0.1.9", md5="743655b276f5e48e04f15cdcbf6c70ab")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
