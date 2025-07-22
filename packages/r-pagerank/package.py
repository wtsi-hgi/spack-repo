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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pageRank_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pageRank/pageRank_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="a1e1f958eb9c7ae6ad9b831d9318ae826f000791f75360c8dc6e4f43235b6c63")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
