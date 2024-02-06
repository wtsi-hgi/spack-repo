# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgraph(RPackage):
	"""Network Analysis and Visualization.

	Routines for simple graphs and network analysis. It can handle large graphs
	very well and provides functions for generating random and regular graphs,
	graph visualization, centrality methods and much more."""

	cran = "igraph"

	version("2.0.1", md5="ee16cb9dcb14e6f65e730ad12bc22846")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pkgconfig@2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cpp11@0.4.7:", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
	depends_on("glpk@4.57:", type=("build", "link", "run"))
