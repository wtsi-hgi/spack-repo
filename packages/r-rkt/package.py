# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkt(RPackage):
	"""Mann-Kendall Test, Seasonal and Regional Kendall Tests

	Contains function rkt which computes the Mann-Kendall test (MK) and the Seasonal and the Regional Kendall Tests for trend (SKT and RKT) and  Theil-Sen's slope estimator. 
	"""
	
	cran = "rkt" 

	version("1.7", md5="7c40fcb9af310d12f800e70b155b2545")

