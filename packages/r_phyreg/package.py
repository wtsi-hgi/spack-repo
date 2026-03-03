# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyreg(RPackage):
	"""The Phylogenetic Regression of Grafen (1989)

	Provides general linear model facilities (single y-variable, multiple x-variables with arbitrary mixture of continuous and categorical and arbitrary interactions) for cross-species data. The method is, however, based on the nowadays rather uncommon situation in which uncertainty about a phylogeny is well represented by adopting a single polytomous tree. The theory is in A. Grafen (1989, Proc. R. Soc. B 326, 119-157) and aims to cope with both recognised phylogeny (closely related species tend to be similar) and unrecognised phylogeny (a polytomy usually indicates ignorance about the true  sequence of binary splits).
	"""
	
	cran = "phyreg" 

	version("1.0.2", md5="24a568d1dc1489b77d369bb2b4ac47f1")

