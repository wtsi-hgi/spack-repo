# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgnewscale(RPackage):
	"""Multiple Fill and Colour Scales in 'ggplot2'.

	Use multiple fill and colour scales in 'ggplot2'."""

	cran = "ggnewscale"

	license("GPL-3.0-only")

	version("0.4.10", md5="a0cf5da106168730a0d0abe5ed4a4c8d")

	depends_on("r-ggplot2@3:", type=("build", "run"))
