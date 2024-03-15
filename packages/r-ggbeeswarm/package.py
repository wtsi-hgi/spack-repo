# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbeeswarm(RPackage):
	"""Categorical Scatter (Violin Point) Plots.

	Provides two methods of plotting categorical scatter plots such that the
	arrangement of points within a category reflects the density of data at
	that region, and avoids over-plotting."""

	cran = "ggbeeswarm"

	license("GPL-3.0-or-later")

	version("0.7.2", md5="b062f40a143df3d06b1865e89544438c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-vipor", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
