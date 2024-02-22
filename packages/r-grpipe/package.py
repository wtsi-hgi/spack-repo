# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpipe(RPackage):
	"""Graphviz Pipeline Plot Based on Grids (grPipe: Graphviz
Pipeline)

	Create a grid-based graphviz using the following functions:
    1 - Creating the data.frame where the nodes are;
    2 - Adding and editing nodes;
    3 - Plotting these nodes.
	"""
	
	cran = "grPipe" 

	version("0.1.0", md5="3e7e4195aaf1b625bfab42c895e4298f")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-diagrammersvg", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
