# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmp(RPackage):
	"""Multiple Precision Arithmetic.

	Multiple Precision Arithmetic (big integers and rationals, prime number
	tests, matrix computation), "arithmetic without limitations" using the C
	library GMP (GNU Multiple Precision Arithmetic)."""

	cran = "gmp"

	version("0.7-4", md5="9d8e130ae524e48d0f62d7db0ac379ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
