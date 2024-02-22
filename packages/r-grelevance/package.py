# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrelevance(RPackage):
	"""Graph-Based k-Sample Comparisons and Relevance Analysis in High
Dimensions

	We propose two distribution-free test statistics based on between-sample edge counts and measure the degree of relevance by standardized counts. Users can set edge costs in the graph to compare the parameters of the distributions. Methods for comparing distributions are as described in: Xiaoping Shi (2021) <arXiv:2107.00728>.
	"""
	
	cran = "GRelevance" 

	version("1.0", md5="a79afb20fde795dd89a35c032da9a193")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
