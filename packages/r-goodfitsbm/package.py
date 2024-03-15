# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoodfitsbm(RPackage):
	"""Monte Carlo Goodness-of-Fit Tests for Stochastic Block Models

	Performing goodness-of-fit tests for stochastic block models used to fit network data. Among the three variants discussed in Karwa et al. (2023) <doi:10.1093/jrsssb/qkad084>, goodness-of-fit test has been performed for the Erdos-Renyi (ER) and Beta versions. 
	"""
	
	homepage = "https://github.com/Roy-SR-007/GoodFitSBM"
	cran = "GoodFitSBM" 

	version("0.0.1", md5="36dbab7a8e299dd4242e157d5b02afc2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
