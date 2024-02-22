# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgraphmatch(RPackage):
	"""Tools for Graph Matching

	Versatile tools and data for graph matching analysis with various forms of prior information
    that supports working with 'igraph' objects, matrix objects, or lists of either.
	"""
	
	homepage = "https://github.com/dpmcsuss/iGraphMatch"
	cran = "iGraphMatch" 

	version("2.0.4", md5="832855f01e091caf9fe98b39a2e84b85")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-clue@0.3.54:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-igraph@1.1.2:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
