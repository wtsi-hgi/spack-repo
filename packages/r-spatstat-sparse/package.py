# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatSparse(RPackage):
	"""Sparse Three-Dimensional Arrays and Linear Algebra Utilities.

	Defines sparse three-dimensional arrays and supports standard operations on
	them. The package also includes utility functions for matrix calculations
	that are common in statistics, such as quadratic forms."""

	cran = "spatstat.sparse"

	version("3.0-3", md5="e62ca18fd36d242b176578688725cac4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.2:", type=("build", "run"))
