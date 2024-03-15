# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtable(RPackage):
	"""Arrange 'Grobs' in Tables.

	Tools to make it easier to work with "tables" of 'grobs'. The 'gtable'
	package defines a 'gtable' grob class that specifies a grid along with a
	list of grobs and their placement in the grid. Further the package makes it
	easy to manipulate and combine 'gtable' objects so that complex
	compositions can be build up sequentially."""

	cran = "gtable"

	license("MIT")

	version("0.3.4", md5="25804ecc0800760da499524ba439fe03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
