# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REntropyestimation(RPackage):
	"""Estimation of Entropy and Related Quantities

	Contains methods for the estimation of Shannon's entropy, variants of Renyi's entropy, mutual information, Kullback-Leibler divergence, and generalized Simpson's indices. The estimators used have a bias that decays exponentially fast. 
	"""
	
	cran = "EntropyEstimation" 

	version("1.2", md5="02763a4615dfdf9f89410f663cdfff68")

