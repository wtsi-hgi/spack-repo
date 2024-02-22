# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcd(RPackage):
	"""Hierarchical Community Detection by Recursive Partitioning

	Hierarchical community detection on networks by a recursive spectral partitioning strategy, which is shown to be effective and efficient in Li, Lei, Bhattacharyya, Sarkar, Bickel, and Levina (2018) <arXiv:1810.01509>. The package also includes a data generating function for a binary tree stochastic block model, a special case of stochastic block model that admits hierarchy between communities.
	"""
	
	cran = "HCD" 

	version("1.0", md5="65fc82d899aab9369b5a37d12d671df3")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-randnet", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
