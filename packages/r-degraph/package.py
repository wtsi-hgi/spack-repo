# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegraph(RPackage):
	"""Two-sample tests on a graph

	DEGraph implements recent hypothesis testing methods which directly assess whether a particular gene network is differentially expressed between two conditions. This is to be contrasted with the more classical two-step approaches which first test individual genes, then test gene sets for enrichment in differentially expressed genes. These recent methods take into account the topology of the network to yield more powerful detection procedures. DEGraph provides methods to easily test all KEGG pathways for differential expression on any gene expression data set and tools to visualize the results.
	"""
	
	bioc = "DEGraph"

	version("1.60.0", commit="a0bf62f0f4c2f4fb7ba91aa08122e64400154e53")
	version("1.54.0", commit="a2666333712b95f98322afd032084a912d9f4b48")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-ncigraph", type=("build", "run"))
