# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfun(RPackage):
	"""Miscellaneous Functions for 'ggplot2'.

	Useful functions to edit 'ggplot' object (e.g., setting fonts for theme and
	layers, adding rounded rectangle as background for each of the legends)."""

	cran = "ggfun"

	license("Artistic-2.0")

	version("0.1.4", md5="a27e5e2c026eba828b588bb230db3ea3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
