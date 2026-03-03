# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfisher(RPackage):
	"""Generalized Fisher's Combination Tests Under Dependence

	Accurate and computationally efficient p-value calculation methods for a general family of Fisher type statistics (GFisher). The GFisher covers Fisher's combination, Good's statistic, Lancaster's statistic, weighted Z-score combination, etc. It allows a flexible weighting scheme, as well as an omnibus procedure that automatically adapts proper weights and degrees of freedom to a given data. The new p-value calculation methods are based on novel ideas of moment-ratio matching and joint-distribution approximation. The technical details can be found in Hong Zhang and Zheyang Wu (2020) <arXiv:2003.01286>. 
	"""
	
	cran = "GFisher" 

	version("0.2.0", md5="893f2e4ca354dc6f5b5d4942e199ac0f")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
