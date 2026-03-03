# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHotDeck(RPackage):
	"""Multiple Hot Deck Imputation

	Performs multiple hot-deck imputation of categorical and continuous variables in a data frame.
	"""
	
	cran = "hot.deck" 

	version("1.2", md5="c110a4e478f619d579d79950d121e069")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
