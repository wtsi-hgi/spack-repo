# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanta(RPackage):
	"""Spatial Analysis of Network Associations

	This package provides methods for measuring the strength of association between a network and a phenotype. It does this by measuring clustering of the phenotype across the network (Knet). Vertices can also be individually ranked by their strength of association with high-weight vertices (Knode).
	"""
	
	bioc = "SANTA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SANTA_2.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SANTA/SANTA_2.38.0.tar.gz"]

	version("2.44.0", tag="RELEASE_3_21")
	version("2.38.0", sha256="1e647f1f8133a7070d83e9661afc7ea11ba8845922c07a518e3ab1212f88a93e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
