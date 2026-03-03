# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperg(RPackage):
	"""Hypergraphs in R

	Implements various tools for storing and analyzing hypergraphs.
  Handles basic undirected, unweighted hypergraphs, and various ways of 
  creating hypergraphs from a number of representations, and
  converting between graphs and hypergraphs.
	"""
	
	cran = "HyperG" 

	version("1.0.0", md5="efe4d54f75d021738beacf19f90f43c3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
