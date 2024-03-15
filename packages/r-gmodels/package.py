# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmodels(RPackage):
	"""Various R programming tools for model fitting."""

	cran = "gmodels"

	license("GPL-2.0-only")

	version("2.19.1", md5="15ae7d7e6190ec8b7cac1ce4446d172b")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
