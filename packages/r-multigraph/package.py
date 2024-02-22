# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultigraph(RPackage):
	"""Plot and Manipulate Multigraphs

	Functions to plot and manipulate multigraphs, signed and valued graphs, bipartite graphs, multilevel graphs, and Cayley graphs with various layout options. 
	"""
	
	homepage = "https://github.com/mplex/multigraph/"
	cran = "multigraph" 

	version("0.99", md5="79321544a0b5199aafbfa5042b4127dc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-multiplex@3:", type=("build", "run"))
