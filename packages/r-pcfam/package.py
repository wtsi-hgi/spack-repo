# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcfam(RPackage):
	"""Computation of Ancestry Scores with Mixed Families and Unrelated
Individuals

	We provide several algorithms to compute the genotype ancestry scores (such as eigenvector projections) in the case where highly correlated individuals are involved.
	"""
	
	cran = "PCFAM" 

	version("1.0", md5="bcb12ff9232d920d1cb19f682ac2c33a")

