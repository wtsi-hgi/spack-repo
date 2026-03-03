# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrca(RPackage):
	"""Computation of Graphlet Orbit Counts in Sparse Graphs

	Implements orbit counting using a fast combinatorial approach.
	Counts orbits of nodes and edges from edge matrix or data frame, or a
	graph object from the graph package.
	"""
	
	cran = "orca" 

	version("1.1-2", md5="f04f052f5890bf5d8e04dc2e61460fe9")

	depends_on("r@3.1:", type=("build", "run"))
