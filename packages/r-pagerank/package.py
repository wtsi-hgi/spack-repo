# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagerank(RPackage):
	"""Temporal and Multiplex PageRank for Gene Regulatory Network Analysis

	Implemented temporal PageRank analysis as defined by Rozenshtein and Gionis. Implemented multiplex PageRank as defined by Halu et al. Applied temporal and multiplex PageRank in gene regulatory network analysis.
	"""
	
	homepage = "https://github.com/hd2326/pageRank"
	bioc = "pageRank"

	version("1.18.0", commit="c16175855fa9255fc1ad9eabbc6c55a8ce6e3f87")
	version("1.12.0", commit="0fb8df7c3a79bf2a991aa2f538331bc736729043")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
