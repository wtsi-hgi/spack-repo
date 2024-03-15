# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinqa(RPackage):
	"""Derivative-free optimization algorithms by quadratic approximation.

	Derivative-free optimization by quadratic approximation based on an
	interface to Fortran implementations by M. J. D. Powell."""

	cran = "minqa"

	license("GPL-2.0-only")

	version("1.2.6", md5="428638718c3146addab57acac73751f0")

	depends_on("r-rcpp", type=("build", "run"))
