# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoissonGlmMix(RPackage):
	"""Fit High Dimensional Mixtures of Poisson GLMs

	Mixtures of Poisson Generalized Linear Models for high dimensional count data clustering. The (multivariate) responses can be partitioned into set of blocks. Three different parameterizations of the linear predictor are considered. The models are estimated according to the EM algorithm with an efficient initialization scheme <doi:10.1016/j.csda.2014.07.005>. 
	"""
	
	cran = "poisson.glm.mix" 

	version("1.4", md5="571b7f19ee5d2cfd2a7f5748dfc592a7")

