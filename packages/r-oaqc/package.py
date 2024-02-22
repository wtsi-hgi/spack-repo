# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROaqc(RPackage):
	"""Computation of the Orbit-Aware Quad Census

	Implements the efficient algorithm by Ortmann and Brandes (2017)
  <doi:10.1007/s41109-017-0027-2> to compute the orbit-aware frequency distribution of induced and non-induced quads, i.e. subgraphs of size four. Given an edge matrix, data frame, or a graph object (e.g., 'igraph'), the orbit-aware counts are computed respective each of the edges and nodes.
	"""
	
	cran = "oaqc" 

	version("1.0", md5="035a9d6aebcc688ab3cb16d3d47a28cd")

	depends_on("r@3.4:", type=("build", "run"))
