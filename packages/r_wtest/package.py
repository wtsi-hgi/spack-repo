# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWtest(RPackage):
	"""The W-Test for Genetic Interactions Testing

	Perform the calculation of W-test, diagnostic checking, calculate
    minor allele frequency (MAF) and odds ratio.
	"""
	
	cran = "wtest" 

	version("3.2", md5="b44bd22f849e253d8efdfc0741bdedb5")

