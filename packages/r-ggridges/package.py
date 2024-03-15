# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgridges(RPackage):
	"""Ridgeline Plots in 'ggplot2'.

	Ridgeline plots provide a convenient way of visualizing changes in
	distributions over time or space. This package enables the creation of such
	plots in 'ggplot2'."""

	cran = "ggridges"

	license("GPL-2.0-only OR custom")

	version("0.5.6", md5="9b895be15340fa000d0e7ebf1045bd33")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
	depends_on("r-withr@2.1.1:", type=("build", "run"))
