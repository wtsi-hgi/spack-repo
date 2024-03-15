# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgraph(RPackage):
	"""An Implementation of Grammar of Graphics for Graphs and Networks.

	The grammar of graphics as implemented in ggplot2 is a poor fit for graph
	and network visualizations due to its reliance on tabular data input.
	ggraph is an extension of the ggplot2 API tailored to graph visualizations
	and provides the same flexible approach to building up plots layer by
	layer."""

	cran = "ggraph"

	license("MIT")

	version("2.2.1", md5="cacb7920286e8197ea44a31749319981")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce@0.3.1:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-graphlayouts@1.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
