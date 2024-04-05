# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaisieprep(RPackage):
	"""Extracts Phylogenetic Island Community Data from Phylogenetic
Trees

	Extracts colonisation and branching times of island
    species to be used for analysis in the R package 'DAISIE'. It uses
    phylogenetic and endemicity data to extract the separate island colonists
    and store them.
	"""
	
	homepage = "https://github.com/joshwlambert/DAISIEprep"
	cran = "DAISIEprep" 

	version("0.4.0", md5="cc1018e939825fa4acf08593a0140286")
	version("0.3.2", md5="0bf1763c11c8496ff444f68a7df9b2bf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-daisie", type=("build", "run"))
	depends_on("r-castor", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
