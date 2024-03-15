# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocfit(RPackage):
	"""Local regression, likelihood and density estimation.

	Local regression, likelihood and density estimation methods as described in
	the 1999 book by Loader."""

	cran = "locfit"

	license("GPL-2.0-or-later")

	version("1.5-9.9", md5="60e6ca00a2b3fbff15f0dbdc0e7f2646")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
