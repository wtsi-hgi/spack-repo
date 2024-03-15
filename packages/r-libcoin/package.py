# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibcoin(RPackage):
	"""Linear Test Statistics for Permutation Inference.

	Basic infrastructure for linear test statistics and permutation inference
	in the framework of Strasser and Weber (1999) <https://epub.wu.ac.at/102/>.
	This package must not be used by end-users.  CRAN package 'coin' implements
	all user interfaces and is ready to be used by anyone."""

	cran = "libcoin"

	license("GPL-2.0-only")

	version("1.0-10", md5="36dbba586a222ba373b5b8bbc61729c4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
