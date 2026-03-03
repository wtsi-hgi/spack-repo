# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowInt(RPackage):
	"""Binary Exponentiation

	Fast exponentiation when the exponent is an integer.
	"""
	
	cran = "pow.int" 

	version("1.3", md5="e8889d4d975452905e31803f4ecae01b")

	depends_on("r@3:", type=("build", "run"))
