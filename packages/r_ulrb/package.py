# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUlrb(RPackage):
	"""Unsupervised Learning Based Definition of Microbial Rare
Biosphere

	A tool to define rare biosphere. 'ulrb' solves the problem of the 
    definition of rarity by replacing human decision with an unsupervised machine 
    learning algorithm (partitioning around medoids, or k-medoids). This algorithm 
    works for any type of microbiome data, provided there is an abundance score 
    for each phylogenetic unit. For validation of this method to several kinds of 
    molecular data and environments, please see Pascoal et al, 2023 (in preparation).
    Preliminary data suggest this method also works well for non-microbiome data, 
    if there is a species abundance table.
	"""
	
	homepage = "https://pascoalf.github.io/ulrb/"
	cran = "ulrb" 

	version("0.1.3", md5="536f5e7e5bcc688fc8cc19a3668fc7a4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
