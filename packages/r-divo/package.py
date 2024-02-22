# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivo(RPackage):
	"""Tools for Analysis of Diversity and Similarity in Biological
Systems

	A set of tools for empirical analysis of diversity (a number and frequency of different types in population) and similarity (a number and frequency of shared types in two populations) in biological or ecological systems. 
	"""
	
	cran = "divo" 

	version("1.0.1", md5="7261dc317b3dc5b4a91a129d9d29fc83")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
