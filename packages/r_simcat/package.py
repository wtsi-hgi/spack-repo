# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcat(RPackage):
	"""Implements Computerized Adaptive Testing Simulations

	Computerized Adaptive Testing simulations with dichotomous and polytomous items. Selects items with Maximum Fisher Information method or randomly, with or without constraints (content balancing and item exposure control). Evaluates the simulation results in terms of precision, item exposure, and test length. Inspired on Magis & Barrada (2017) <doi:10.18637/jss.v076.c01>.
	"""
	
	homepage = "https://github.com/alexandrejaloto/simCAT"
	cran = "simCAT" 

	version("1.0.0", md5="0c87216f46b2c48dbaccf00bcbba3707")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-mirtcat", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
