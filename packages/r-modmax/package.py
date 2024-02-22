# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModmax(RPackage):
	"""Community Structure Detection via Modularity Maximization

	The algorithms implemented here are used to detect the community structure of a network. 
            These algorithms follow different approaches, but are all based on the concept of modularity maximization.
	"""
	
	cran = "modMax" 

	version("1.1", md5="aad19bd3064327ed354278484b883f67")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
