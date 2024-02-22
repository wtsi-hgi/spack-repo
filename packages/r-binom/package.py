# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinom(RPackage):
	"""Binomial Confidence Intervals for Several Parameterizations

	Constructs confidence intervals on the probability of
        success in a binomial experiment via several parameterizations.
	"""
	
	cran = "binom" 

	version("1.1-1.1", md5="6d9cbf4fa0fe82414417f2286d1007b5")

