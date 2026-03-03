# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdst(RPackage):
	"""Data Driven Smooth Tests

	Smooth testing of goodness of fit. These tests are data
    driven (alternative hypothesis is dynamically selected based on data). In this
    package you will find various tests for exponent, Gaussian, Gumbel and uniform
    distribution.
	"""
	
	cran = "ddst" 

	version("1.4", md5="3429c6074f4542c2da274b1d0ccd6ff1")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
