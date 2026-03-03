# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDupnodes(RPackage):
	"""Creates an 'igraph' Object that Duplicates Nodes with Self-Loops

	Creates a new graph from an existing one, duplicating nodes
    with self-loops. This can be used for a computation of betweenness
    centrality that does not drop this essential information. Implements
    Merelo & Molinari (2024) <doi:10.1007/s42001-023-00245-4>.
	"""
	
	cran = "dupNodes" 

	version("0.2.0", md5="59310417d64e6bbaa9fd65291d680158")
	version("0.1.0", md5="aa33311f1f3f0b40a0ee982e04ac4512")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dogesr", type=("build", "run"))
