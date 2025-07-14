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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LinkHD_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LinkHD/LinkHD_1.16.0.tar.gz"]

    version("1.22.0", tag="RELEASE_3_21")
	version("1.16.0", sha256="8e1cbeb2208d40330ffb2a8492523929b04611ff3ac0d901ee9d89bbaadf81c5")

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
