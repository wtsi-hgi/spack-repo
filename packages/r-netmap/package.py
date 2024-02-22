# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetmap(RPackage):
	"""Represent Network Objects on a Map

	Represent 'network' or 'igraph' objects whose vertices can be represented by features in an 'sf' object as a network graph surmising a 'sf' plot. Fits into 'ggplot2' grammar.
	"""
	
	homepage = "https://github.com/artod83/netmap"
	cran = "netmap" 

	version("0.1.3", md5="fb2eadae027fe37e01df8c7744d2086b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
