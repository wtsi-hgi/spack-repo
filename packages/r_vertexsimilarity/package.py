# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVertexsimilarity(RPackage):
	"""Creates Vertex Similarity Matrix for an Undirected Graph

	Creates Vertex Similarity matrix of an undirected graph based
  on the method stated by E. A. Leicht, Petter Holme, AND M. E. J. Newman in
  their paper <DOI:10.1103/PhysRevE.73.026120>.
	"""
	
	cran = "VertexSimilarity" 

	version("0.1", md5="23d82a578bceea333ff93514d0236c5f")

	depends_on("r-igraph", type=("build", "run"))
