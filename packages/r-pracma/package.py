# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPracma(RPackage):
	"""Practical Numerical Math Functions.

	Provides a large number of functions from numerical analysis and linear
	algebra, numerical optimization, differential equations, time series, plus
	some well-known special mathematical functions. Uses 'MATLAB' function
	names where appropriate to simplify porting."""

	cran = "pracma"

	license("GPL-3.0-or-later")

	version("2.4.4", md5="f45e85a91a5e14b56a86191dd0bc9abd")

	depends_on("r@3.1:", type=("build", "run"))
