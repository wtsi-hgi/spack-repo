# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoband(RPackage):
	"""Generate Isolines and Isobands from Regularly Spaced Elevation Grids.

	A fast C++ implementation to generate contour lines (isolines) and contour
	polygons (isobands) from regularly spaced grids containing elevation
	data."""

	cran = "isoband"

	version("0.2.7", md5="7241f95bafb46b44aa380b9a71b10467")

