# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmst(RPackage):
	"""A Toolbox for the Multi-Criteria Minimum Spanning Tree Problem

	Algorithms to approximate the Pareto-front of multi-criteria minimum spanning tree problems.
	"""
	
	homepage = "https://github.com/jakobbossek/mcMST"
	cran = "mcMST" 

	version("1.1.1", md5="9ba7ed114a8fbb01453ebc7abb92e811")

	depends_on("r-bbmisc@1.6:", type=("build", "run"))
	depends_on("r-ecr@2.1:", type=("build", "run"))
	depends_on("r-grapherator", type=("build", "run"))
	depends_on("r-checkmate@1.1:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
