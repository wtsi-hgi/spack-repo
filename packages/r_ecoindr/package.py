# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcoindr(RPackage):
	"""Ecological Indicators

	Calculates several indices, such as of diversity, fluctuation, etc., and they are used to estimate ecological indicators.
	"""
	
	cran = "EcoIndR" 

	version("2.0", md5="1bb0e62d2cfb2da1f626240c3e6ad4b7")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-rarity", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
