# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRUtils(RPackage):
	"""Various Programming Utilities.

	Utility functions useful when programming and developing R packages."""

	cran = "R.utils"

	version("2.12.3", md5="c76bb7365b00306ed536d8151d380594")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
