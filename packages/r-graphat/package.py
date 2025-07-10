# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphat(RPackage):
	"""Graph Theoretic Association Tests

	Functions and data used in Balasubramanian, et al. (2004)
	"""
	
	bioc = "GraphAT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GraphAT_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GraphAT/GraphAT_1.74.0.tar.gz"]

	version("1.74.0", sha256="0e5d6488d4b833cf51f1554989f69dc3ae8eee55efd3b8b232895926b8f9b2e4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
