# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChaosgame(RPackage):
	"""Chaos Game

	The main objective of the package is to enter a word of at least two letters based on which an Iterated Function System with Probabilities is constructed, and a two-dimensional fractal containing the chosen word infinitely often is generated via the Chaos Game. Additionally, the package allows to project the two-dimensional fractal on several three-dimensional surfaces and to transform the fractal into another fractal with uniform marginals.
	"""
	
	cran = "ChaosGame" 

	version("1.4", md5="d63e5b7911bdae9062aa6fc5cbfd1786")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
