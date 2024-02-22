# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunwithnumbers(RPackage):
	"""Fun with Fractions and Number Sequences

	A collection of toys to do things like generate Collatz sequences, convert a fraction to "continued fraction" form, calculate a fraction which is a close approximation to some value (e.g., 22/7 or 355/113 for pi), and so on.
	"""
	
	cran = "FunWithNumbers" 

	version("1.1.1", md5="f509a9a24e2c9d15209dac0160140de6")

	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
