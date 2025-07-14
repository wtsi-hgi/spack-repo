# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkhd(RPackage):
	"""LinkHD: a versatile framework to explore and integrate heterogeneous data

	Here we present Link-HD, an approach to integrate heterogeneous datasets, as a generalization of STATIS-ACT (“Structuration des Tableaux A Trois Indices de la Statistique–Analyse Conjointe de Tableaux”), a family of methods to join and compare information from multiple subspaces. However, STATIS-ACT has some drawbacks since it only allows continuous data and it is unable to establish relationships between samples and features. In order to tackle these constraints, we incorporate multiple distance options and a linear regression based Biplot model in order to stablish relationships between observations and variable and perform variable selection.
	"""
	
	bioc = "LinkHD"

	version("1.22.0", commit="86759cc762a3fec898368fd52dcc7cb82483eba8")
	version("1.16.0", commit="c153185b29d7a5d65026406763ca6caf16de318a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
