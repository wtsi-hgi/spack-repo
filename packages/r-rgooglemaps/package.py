# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgooglemaps(RPackage):
	"""Overlays on Static Maps.

	This package serves two purposes: (i) Provide a comfortable R interface to
	query the Google server for static maps, and (ii) Use the map as a
	background image to overlay plots within R. This requires proper coordinate
	scaling."""

	cran = "RgoogleMaps"

	version("1.5.1", md5="e1c161a7daed4d7aaef73d5005e97be1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
