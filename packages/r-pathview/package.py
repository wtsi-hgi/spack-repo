# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathview(RPackage):
	"""a tool set for pathway based data integration and visualization.

	Pathview is a tool set for pathway based data integration and
	visualization. It maps and renders a wide variety of biological data on
	relevant pathway graphs. All users need is to supply their data and
	specify the target pathway. Pathview automatically downloads the pathway
	graph data, parses the data file, maps user data to the pathway, and
	render pathway graph with the mapped data. In addition, Pathview also
	seamlessly integrates with pathway and gene set (enrichment) analysis
	tools for large-scale and fully automated analysis."""

	bioc = "pathview"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/pathview_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/pathview/pathview_1.42.0.tar.gz"]

	version("1.42.0", md5="5e17ceee29bb13083a2b11be28edacb0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kegggraph", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
