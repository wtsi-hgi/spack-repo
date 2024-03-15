# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKegggraph(RPackage):
	"""KEGGgraph: A graph approach to KEGG PATHWAY in R and Bioconductor.

	KEGGGraph is an interface between KEGG pathway and graph object as well
	as a collection of tools to analyze, dissect and visualize these graphs.
	It parses the regularly updated KGML (KEGG XML) files into graph models
	maintaining all essential pathway attributes. The package offers
	functionalities including parsing, graph operation, visualization and
	etc."""

	bioc = "KEGGgraph"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/KEGGgraph_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/KEGGgraph/KEGGgraph_1.62.0.tar.gz"]

	version("1.62.0", md5="9a4fb63b5bab3eeb0af51af22fa2dc16")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml@2.3.0:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
