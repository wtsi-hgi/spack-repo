# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiagrammer(RPackage):
	"""Graph/Network Visualization.

	Build graph/network structures using functions for stepwise addition and
	deletion of nodes and edges. Work with data available in tables for bulk
	addition of nodes, edges, and associated metadata. Use graph selections and
	traversals to apply changes to specific nodes or edges. A wide selection of
	graph algorithms allow for the analysis of graphs. Visualize the graphs and
	take advantage of any aesthetic properties assigned to nodes and edges."""

	cran = "DiagrammeR"

	version("1.0.11", md5="94ec61b50053de75a748824f67183bcd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-glue@1.5:", type=("build", "run"))
	depends_on("r-htmltools@0.5.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5:", type=("build", "run"))
	depends_on("r-igraph@1.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-readr@2.1.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-viridislite@0.4.2:", type=("build", "run"))
	depends_on("r-visnetwork@2.1:", type=("build", "run"))
