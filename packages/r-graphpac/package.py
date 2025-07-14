# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphpac(RPackage):
	"""Identification of Mutational Clusters in Proteins via a Graph Theoretical Approach.

	Identifies mutational clusters of amino acids in a protein while utilizing the proteins tertiary structure via a graph theoretical model.
	"""
	
	bioc = "GraphPAC"

	version("1.50.0", commit="2e43ebc5f3aadf54704d10bd8459cfb383d1fd9e")
	version("1.44.0", commit="f5c501d5ead7c1140981de8d82d60a85b0e21ccb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ipac", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-rmallow", type=("build", "run"))
