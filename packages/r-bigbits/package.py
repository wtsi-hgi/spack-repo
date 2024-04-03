# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigbits(RPackage):
	"""Perform Boolean Operations on Large Numbers

	These tools accept integers in any base from 2 to 36, including 2's complement format, and perform actions like "AND," "OR", "NOT", "SHIFTR/L" etc. The output can be in any base specified. A direct base to base converter is included. 
	"""
	
	cran = "bigBits" 

	version("1.1", md5="a66c6befad3436debf6f479bf6b4b302")
	version("1.2", md5="3592bd2d5ed5ec17ed77f80f98bccc97")

	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
