# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcigraph(RPackage):
	"""Pathways from the NCI Pathways Database

	Provides various methods to load the pathways from the NCI Pathways Database in R graph objects and to re-format them.
	"""
	
	bioc = "NCIgraph" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/NCIgraph_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/NCIgraph/NCIgraph_1.50.0.tar.gz"]

	version("1.50.0", md5="ed568ded26dce9e64d5f38606e65c13d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
