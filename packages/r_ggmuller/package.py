# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmuller(RPackage):
	"""Create Muller Plots of Evolutionary Dynamics

	Create plots that combine a phylogeny and frequency dynamics.
    Phylogenetic input can be a generic adjacency matrix or a tree of class "phylo".
    Inspired by similar plots in publications of the labs of RE Lenski and JE
    Barrick. Named for HJ Muller (who popularised such plots) and H Wickham (whose
    code this package exploits).
	"""
	
	cran = "ggmuller" 

	version("0.5.6", md5="d69d1bf491d756b6e131d2b9fabe1b1d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
