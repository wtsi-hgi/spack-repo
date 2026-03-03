# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesirability(RPackage):
	"""Function Optimization and Ranking via Desirability Functions

	S3 classes for multivariate optimization using the desirability function by Derringer and Suich (1980).
	"""
	
	homepage = "https://github.com/topepo/desirability"
	cran = "desirability" 

	version("2.1", md5="6597122db76d97f04c66556d66bbd2d5")

