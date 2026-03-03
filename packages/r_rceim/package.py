# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRceim(RPackage):
	"""R Cross Entropy Inspired Method for Optimization

	An implementation of a stochastic heuristic method for performing multidimensional function optimization. The method is inspired in the Cross-Entropy Method. It does not relies on derivatives, neither imposes particularly strong requirements into the function to be optimized. Additionally, it takes profit from multi-core processing to enable optimization of time-consuming functions.
	"""
	
	cran = "RCEIM" 

	version("0.3", md5="a7d8fd7d99fce1798c56d5e683b55032")

