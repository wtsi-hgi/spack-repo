# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutests(RPackage):
	"""Approximate Unconditional and Permutation Tests

	Performs approximate unconditional and permutation testing for
    2x2 contingency tables. Motivated by testing for disease association with rare
    genetic variants in case-control studies. When variants are extremely rare,
    these tests give better control of Type I error than standard tests.
	"""
	
	cran = "AUtests" 

	version("0.99", md5="59b60bafd7feb1997c813aef0ac0c7fc")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
