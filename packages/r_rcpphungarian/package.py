# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpphungarian(RPackage):
	"""Solves Minimum Cost Bipartite Matching Problems

	Header library and R functions to solve minimum cost bipartite matching problem 
 using Huhn-Munkres algorithm (Hungarian algorithm; <https://en.wikipedia.org/wiki/Hungarian_algorithm>;
 Kuhn (1955) <doi:10.1002/nav.3800020109>). 
 This is a repackaging of code written by Cong Ma in the GitHub repo <https://github.com/mcximing/hungarian-algorithm-cpp>.
	"""
	
	homepage = "https://github.com/jsilve24/RcppHungarian"
	cran = "RcppHungarian" 

	version("0.3", md5="1ca77b7707cb433d5ce9a0fa1f58b8cf")

	depends_on("r-rcpp", type=("build", "run"))
