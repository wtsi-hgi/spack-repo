# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffnet(RPackage):
	"""Identifying Significant Node Scores using Network Diffusion
Algorithm

	Designed for network analysis, leveraging the personalized PageRank algorithm to calculate node scores in a given graph. This innovative approach allows users to uncover the importance of nodes based on a customized perspective, making it particularly useful in fields like bioinformatics, social network analysis, and more.
	"""
	
	cran = "DiffNet" 

	version("1.0.2", md5="f522d2572f9587be96ad108e04829070")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
