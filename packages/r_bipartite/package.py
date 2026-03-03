# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBipartite(RPackage):
	"""Visualising Bipartite Networks and Calculating Some (Ecological)
Indices

	Functions to visualise webs and calculate a series of indices commonly used to describe pattern in (ecological) webs. It focuses on webs consisting of only two levels (bipartite), e.g. pollination webs or predator-prey-webs. Visualisation is important to get an idea of what we are actually looking at, while the indices summarise different aspects of the web's topology. 
	"""
	
	homepage = "https://github.com/biometry/bipartite"
	cran = "bipartite" 

	version("2.19", md5="ef6592e3dbcf69bcb5bd6cc968c19766")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
