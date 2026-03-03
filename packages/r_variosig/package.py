# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariosig(RPackage):
	"""Testing Spatial Dependence Using Empirical Variogram

	Applying Monte Carlo permutation to generate pointwise variogram envelope and checking for spatial dependence at different scales using permutation test. Empirical Brown's method and Fisher's method are used to compute overall p-value for hypothesis test.
	"""
	
	cran = "variosig" 

	version("0.3-1", md5="cbc94a099e7c7b4ef1724b21d9a36197")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
