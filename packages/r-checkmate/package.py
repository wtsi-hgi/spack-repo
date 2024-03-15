# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckmate(RPackage):
	"""Fast and Versatile Argument Checks.

	Tests and assertions to perform frequent argument checks.  A substantial
	part of the package was written in C to minimize any worries about
	execution time overhead."""

	cran = "checkmate"

	license("BSD-3-Clause")

	version("2.3.1", md5="187badb003e010483a10dd43a084592d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-backports@1.1:", type=("build", "run"))
