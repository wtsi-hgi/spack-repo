# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgraph6(RPackage):
	"""Representing Graphs as 'graph6', 'digraph6' or 'sparse6' Strings

	Encode network data as strings of printable ASCII characters. Implemented 
    functions include encoding and decoding adjacency matrices, edgelists, igraph, and
    network objects to/from formats 'graph6', 'sparse6', and 'digraph6'. The formats and
    methods are described in McKay, B.D. and Piperno, A (2014)
    <doi:10.1016/j.jsc.2013.09.003>.
	"""
	
	homepage = "https://mbojan.github.io/rgraph6/"
	cran = "rgraph6" 

	version("2.0-4", md5="460983e6e101476fcdded161008900a2", url="https://cran.r-project.org/src/contrib/rgraph6_2.0-4.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
