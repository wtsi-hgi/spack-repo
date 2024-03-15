# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScattermore(RPackage):
	"""Scatterplots with More Points.

	C-based conversion of large scatterplot data to rasters. Speeds up plotting
	of data with millions of points."""

	cran = "scattermore"

	license("GPL-3.0-or-later")

	version("1.2", md5="e7d69ed06df297b9e4193d1fb225d3d9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
