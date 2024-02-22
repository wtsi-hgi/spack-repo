# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubcopem2d(RPackage):
	"""Bivariate Empirical Subcopula

	Calculate empirical subcopula and dependence measures from a given bivariate sample, and Bernstein copula approximations.
	"""
	
	cran = "subcopem2D" 

	version("1.3", md5="89958044806f8a4c41a4b4930f0f335f")

