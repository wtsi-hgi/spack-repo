# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCentiserve(RPackage):
	"""Find Graph Centrality Indices

	Calculates centrality indices additional to the 'igraph' package centrality functions.
	"""
	
	homepage = "http://www.centiserver.org/"
	cran = "centiserve" 

	version("1.0.0", md5="1f74abf8548796911048ba2d0adc86ce")

	depends_on("r-igraph@0.7.1:", type=("build", "run"))
	depends_on("r-matrix@1.1.4:", type=("build", "run"))
