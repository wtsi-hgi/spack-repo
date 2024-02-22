# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuclu(RPackage):
	"""Quantile-Based Clustering Algorithms

	Various quantile-based clustering algorithms: algorithm CU (Common theta and Unscaled variables), algorithm CS (Common theta and Scaled variables through lambda_j), algorithm VU (Variable-wise theta_j and Unscaled variables) and algorithm VW (Variable-wise theta_j and Scaled variables through lambda_j). Hennig, C., Viroli, C., Anderlucci, L. (2019) "Quantile-based clustering." Electronic Journal of Statistics. 13 (2) 4849 - 4883  <doi:10.1214/19-EJS1640>.
	"""
	
	cran = "QuClu" 

	version("1.0.1", md5="7eab01769b3f1ab1954cd8618e03eabb")

