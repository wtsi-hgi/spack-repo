# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnt(RPackage):
	"""Affine Invariant Tests of Multivariate Normality

	Various affine invariant multivariate normality tests are provided. It is designed to accompany the survey article Ebner, B. and Henze, N. (2020) <arXiv:2004.07332> titled "Tests for multivariate normality -- a critical review with emphasis on weighted L^2-statistics". We implement new and time honoured L^2-type tests of multivariate normality, such as the Baringhaus-Henze-Epps-Pulley (BHEP) test, the Henze-Zirkler test, the test of Henze-Jiménes-Gamero, the test of Henze-Jiménes-Gamero-Meintanis, the test of Henze-Visage, the Dörr-Ebner-Henze test based on harmonic oscillator and the Dörr-Ebner-Henze test based on a double estimation in a PDE. Secondly, we include the measures of multivariate skewness and kurtosis by Mardia, Koziol, Malkovich and Afifi and Móri, Rohatgi and Székely, as well as the associated tests. Thirdly, we include the tests of multivariate normality by Cox and Small, the 'energy' test of Székely and Rizzo, the tests based on spherical harmonics by Manzotti and Quiroz and the test of Pudelko. All the functions and tests need the data to be a n x d matrix where n is the samplesize (number of rows) and d is the dimension (number of columns).
	"""
	
	cran = "mnt" 

	version("1.3", md5="c4fe835a3632d760c385139591607bc2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
