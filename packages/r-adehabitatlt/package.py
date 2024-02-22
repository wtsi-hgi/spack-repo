# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdehabitatlt(RPackage):
	"""Analysis of Animal Movements

	A collection of tools for the analysis of animal movements.
	"""
	
	cran = "adehabitatLT" 

	version("0.3.27", md5="1edaafee1f29d3696f121d727492d1c9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-adehabitatma", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
