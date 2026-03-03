# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcmm(RPackage):
	"""Empirical Bayes Variable Selection via ICM/M Algorithm

	Empirical Bayes variable selection via ICM/M algorithm for normal, binary logistic, and Cox's regression. The basic problem is to fit high-dimensional regression which sparse coefficients. This package allows incorporating the Ising prior to capture structure of predictors in the modeling process. More information can be found in the papers listed in the URL below.
	"""
	
	homepage = "https://www.researchgate.net/publication/279279744_Selecting_massive_variables_using_an_iterated_conditional_modesmedians_algorithm"
	cran = "icmm" 

	version("1.2", md5="e196ace4ba277da2d6b35a85dedf0e79")

	depends_on("r-ebayesthresh", type=("build", "run"))
