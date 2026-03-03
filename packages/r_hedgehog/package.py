# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHedgehog(RPackage):
	"""Property-Based Testing

	Hedgehog will eat all your bugs.
  'Hedgehog' is a property-based testing package in the spirit
  of 'QuickCheck'. With 'Hedgehog', one can test properties
  of their programs against randomly generated input, providing
  far superior test coverage compared to unit testing. One of the
  key benefits of 'Hedgehog' is integrated shrinking of
  counterexamples, which allows one to quickly find the cause of
  bugs, given salient examples when incorrect behaviour occurs.
	"""
	
	homepage = "https://hedgehog.qa"
	cran = "hedgehog" 

	version("0.1", md5="97f4ac99db5608d7538fbe1378491ebc")

	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rlang@0.1.6:", type=("build", "run"))
