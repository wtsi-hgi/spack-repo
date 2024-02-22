# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFraction(RPackage):
	"""Numeric Number into Fraction

	Turn numeric,data.frame,matrix into fraction form.
	"""
	
	cran = "FRACTION" 

	version("1.1.1", md5="726fbb6fe6e0f3ab4872cbd6037084a4")

