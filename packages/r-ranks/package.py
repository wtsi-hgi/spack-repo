# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRanks(RPackage):
	"""Ranking of Nodes with Kernelized Score Functions

	Implementation of Kernelized score functions and other semi-supervised learning algorithms for node label ranking to analyze  biomolecular networks. RANKS can be easily applied to a large set of different relevant problems in computational biology, ranging from automatic protein function prediction, to gene disease prioritization and drug repositioning, and more in general to any bioinformatics problem that can be formalized as a node label ranking problem in a graph. The modular nature of the implementation allows to experiment with different score functions and kernels and to easily compare the results with baseline network-based methods such as label propagation and random walk algorithms, as well as to enlarge the algorithmic scheme by adding novel user-defined score functions and kernels.
	"""
	
	cran = "RANKS" 

	version("1.1", md5="5b18423ec33f48ed312469efdfce9152")

	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-netpreproc", type=("build", "run"))
	depends_on("r-perfmeas", type=("build", "run"))
