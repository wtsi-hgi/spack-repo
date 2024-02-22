# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenord(RPackage):
	"""Simulation of Discrete Random Variables with Given Correlation
Matrix and Marginal Distributions

	A gaussian copula based procedure for generating samples from discrete random variables with prescribed correlation matrix and marginal distributions.
	"""
	
	cran = "GenOrd" 

	version("1.4.0", md5="2e7771f55ab51f5950cb021fb0a546ac")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
