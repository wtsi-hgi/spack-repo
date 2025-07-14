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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NCIgraph_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NCIgraph/NCIgraph_1.50.0.tar.gz"]

	version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="661bebfac48019277075f230d08b25a64ae99f867903faef3e769ba1c0c8698a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
