# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegan(RPackage):
	"""Community Ecology Package.

	Ordination methods, diversity analysis and other functions for community
	and vegetation ecologists."""

	cran = "vegan"

	license("GPL-2.0-only")

	version("2.6-4", md5="3e8bff267537730be8ec6dd3970a2b4a")

	depends_on("r-permute@0.9.0:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
