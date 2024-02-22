# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylotop(RPackage):
	"""Calculating Topological Properties of Phylogenies

	Tools for calculating and viewing topological properties of phylogenetic trees.
	"""
	
	homepage = "https://michellekendall.github.io/phyloTop/"
	cran = "phyloTop" 

	version("2.1.2", md5="b6a1d9d2b3107b276b596579bb2bd385")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nhpoisson", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
