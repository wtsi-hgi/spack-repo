# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactranktests(RPackage):
	"""Exact Distributions for Rank and Permutation Tests

	Computes exact conditional p-values and quantiles using an
 implementation of the Shift-Algorithm by Streitberg & Roehmel.
	"""
	
	cran = "exactRankTests" 

	version("0.8-35", md5="5c3767db5ff0c9d69b9990d4443f0cad")

	depends_on("r@2.4:", type=("build", "run"))
