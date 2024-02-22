# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtd(RPackage):
	"""A Method for 'Connecting The Dots' in Weighted Graphs

	A method for pattern discovery in weighted graphs as outlined in Thistlethwaite et al. (2021) <doi:10.1371/journal.pcbi.1008550>. Two use cases are achieved: 1) Given a weighted graph and a subset of its nodes, do the nodes show significant connectedness? 2) Given a weighted graph and two subsets of its nodes, are the subsets close neighbors or distant?
	"""
	
	cran = "CTD" 

	version("1.2", md5="a016257a551a2a639afa4b2a6fa7a61e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
