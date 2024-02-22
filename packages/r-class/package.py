# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClass(RPackage):
	"""Functions for Classification.

	Various functions for classification, including k-nearest neighbour,
	Learning Vector Quantization and Self-Organizing Maps."""

	cran = "class"

	version("7.3-22", md5="8b205d2ef6196c1c637b9d62ee026551")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
