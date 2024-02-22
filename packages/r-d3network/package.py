# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3network(RPackage):
	"""Tools for creating D3 JavaScript network, tree, dendrogram, and
Sankey graphs from R

	This packages is intended to make it easy to create D3 JavaScript
    network, tree, dendrogram, and Sankey graphs from R using data frames.
    !!! NOTE: Active development has moved to the networkD3 package. !!!
	"""
	
	homepage = "http://christophergandrud.github.io/d3Network/"
	cran = "d3Network" 

	version("0.5.2.1", md5="32fb769bbbcb5fb7eab98612dddaf441")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
