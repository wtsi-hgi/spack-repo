# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmpfr(RPackage):
	"""R MPFR - Multiple Precision Floating-Point Reliable.

	Arithmetic (via S4 classes and methods) for arbitrary precision floating
	point numbers, including transcendental ("special") functions. To this end,
	Rmpfr interfaces to the LGPL'ed MPFR (Multiple Precision Floating-Point
	Reliable) Library which itself is based on the GMP (GNU Multiple Precision)
	Library."""

	cran = "Rmpfr"

	version("0.9-5", md5="d20d82b6a05cac1bb46dbd53f82a2d1f")

	depends_on("r-gmp@0.6.1:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
	depends_on("mpfr@3.0.0:", type=("build", "link", "run"))
