# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVizdraws(RPackage):
	"""Visualize Draws from the Prior and Posterior Distributions

	Interactive visualization for Bayesian prior and posterior distributions. 
    This package facilitates an animated transition between prior and posterior distributions. 
    Additionally, it splits the distribution into bars based on the provided 'breaks,' displaying 
    the probability for each region. If no 'breaks' are provided, it defaults to zero.
	"""
	
	homepage = "https://github.com/ignacio82/vizdraws/"
	cran = "vizdraws" 

	version("2.0.0", md5="b7d087a2e974445499cb768ac0e07d5d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
