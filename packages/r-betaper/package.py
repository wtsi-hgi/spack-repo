# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetaper(RPackage):
	"""Taxonomic Uncertainty on Multivariate Analyses of Ecological
Data

	Permutational method to incorporate taxonomic uncertainty  and some functions to assess its effects on parameters of some widely used multivariate methods in ecology, as explained in Cayuela et al. (2011) <doi:10.1111/j.1600-0587.2009.05899.x>.
	"""
	
	cran = "betaper" 

	version("1.1-2", md5="6a1a93fb525bb85b6e3fdb05ec9ec7c5")

	depends_on("r-vegan", type=("build", "run"))
