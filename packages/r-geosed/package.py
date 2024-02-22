# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosed(RPackage):
	"""Smallest Enclosing Disc for Latitude and Longitude Points

	
    Find the smallest circle that contains all longitude and latitude input points. From the generated center and radius, variable side polygons can be created, navigation based on bearing and distance can be applied, and more. Based on a modified version of Welzl's algorithm for smallest circle. Distance calculations are based on the haversine formula. Calculations for distance, midpoint, bearing and more are derived from <https://www.movable-type.co.uk>.
	"""
	
	cran = "geosed" 

	version("0.1.1", md5="a0f7fe8b74a25fe41c509acd307c3ce7")

