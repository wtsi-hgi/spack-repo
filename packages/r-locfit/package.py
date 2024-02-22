# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocfit(RPackage):
	"""Local regression, likelihood and density estimation.

	Local regression, likelihood and density estimation methods as described in
	the 1999 book by Loader."""

	cran = "locfit"

	version("1.5-9.8", md5="fd900b88abdee96d0d9afac8ec753db1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
