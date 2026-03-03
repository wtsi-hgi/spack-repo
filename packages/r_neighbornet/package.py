# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeighbornet(RPackage):
	"""Neighbor_net analysis

	Identify the putative mechanism explaining the active interactions between genes in the investigated phenotype.
	"""
	
	bioc = "NeighborNet" 

	version("1.20.0", commit="3f5d90e33dd47c32296042433b482d6c50c3e7a1")

	depends_on("r-graph", type=("build", "run"))
