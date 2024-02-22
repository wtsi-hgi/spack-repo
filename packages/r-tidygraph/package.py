# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygraph(RPackage):
	"""A Tidy API for Graph Manipulation.

	A graph, while not "tidy" in itself, can be thought of as two tidy data
	frames describing node and edge data respectively. 'tidygraph' provides an
	approach to manipulate these two virtual data frames using the API defined
	in the 'dplyr' package, as well as provides tidy interfaces to a lot of
	common graph algorithms."""

	cran = "tidygraph"

	version("1.3.1", md5="e1995b3e38c2acdaa96376ad13f33d04")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-igraph@2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
