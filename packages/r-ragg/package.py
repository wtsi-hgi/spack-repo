# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagg(RPackage):
	"""Graphic Devices Based on AGG.

	Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D drawing
	library. The 'ragg' package provides a set of graphic devices based on AGG
	to use as alternative to the raster devices provided through the
	'grDevices' package."""

	cran = "ragg"

	license("MIT")

	version("1.3.0", md5="dc546005cff17506bf712be3e7dbf610")

	depends_on("r-systemfonts", type=("build", "run"))
	depends_on("r-textshaping", type=("build", "run"))
	depends_on("freetype@2:", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
