# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrapherator(RPackage):
	"""A Modular Multi-Step Graph Generator

	Set of functions for step-wise generation of (weighted) graphs. Aimed for research in the field of single- and multi-objective combinatorial optimization. Graphs are generated adding nodes, edges and weights. Each step may be repeated multiple times with different predefined and custom generators resulting in high flexibility regarding the graph topology and structure of edge weights.
	"""
	
	homepage = "https://github.com/jakobbossek/grapherator"
	cran = "grapherator" 

	version("1.0.0", md5="a54194f105f33cb7e855c55002b5df32")

	depends_on("r-bbmisc@1.6:", type=("build", "run"))
	depends_on("r-checkmate@1.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
