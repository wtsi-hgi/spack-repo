# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxmatching(RPackage):
	"""Maximum Matching for General Weighted Graph

	Computes the maximum matching for unweighted graph and maximum
    matching for (un)weighted bipartite graph efficiently.
	"""
	
	cran = "maxmatching" 

	version("0.1.0", md5="20b358e46f44a508c27b60624bf47669")

	depends_on("r-igraph", type=("build", "run"))
