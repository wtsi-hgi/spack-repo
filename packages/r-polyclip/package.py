# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyclip(RPackage):
	"""Polygon Clipping.

	R port of Angus Johnson's open source library Clipper. Performs polygon
	clipping operations (intersection, union, set minus, set difference) for
	polygonal regions of arbitrary complexity, including holes. Computes offset
	polygons (spatial buffer zones, morphological dilations, Minkowski
	dilations) for polygonal regions and polygonal lines. Computes Minkowski
	Sum of general polygons. There is a function for removing
	self-intersections from polygon data."""

	cran = "polyclip"

	license("BSL-1.0")

	version("1.10-6", md5="847eb50bb15aa4b2960d2b65227aab92")

	depends_on("r@3:", type=("build", "run"))
