# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWto(RPackage):
	"""Computing Weighted Topological Overlaps (wTO) & Consensus wTO
Network

	Computes the Weighted Topological Overlap with positive and negative signs (wTO) networks given a data frame containing the mRNA count/ expression/ abundance per sample, and a vector containing the interested nodes of interaction (a subset of the elements of the full data frame). It also computes the cut-off threshold or p-value based on the individuals bootstrap or the values reshuffle per individual. It also allows the construction of a consensus network, based on multiple wTO networks. The package includes a visualization tool for the networks.  More about the methodology can be found at <arXiv:1711.04702>.
	"""
	
	cran = "wTO" 

	version("2.0.2", md5="d76292d2c856b719b1f21849c6f8af6f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-som", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-hiclimr", type=("build", "run"))
