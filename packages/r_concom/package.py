# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcom(RPackage):
	"""Connected Components of an Undirected Graph

	Provides a function for fast computation of the connected
    components of an undirected graph (though not faster than the
    components() function of the 'igraph' package) from the edges or the
    adjacency matrix of the graph. Based on this one, a function to
    compute the connected components of a triangle 'rgl' mesh is also
    provided.
	"""
	
	homepage = "https://github.com/stla/concom"
	cran = "concom" 

	version("1.0.0", md5="707ea13df53b41d35125a4c515085544")

	depends_on("r-english", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
