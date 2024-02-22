# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlot3d(RPackage):
	"""Plotting Multi-Dimensional Data.

	Functions for viewing 2-D and 3-D data, including perspective plots, slice
	plots, surface plots, scatter plots, etc. Includes data sets from
	oceanography."""

	cran = "plot3D"

	version("1.4.1", md5="5088aac269c419a0b84509d0f761bdfb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
