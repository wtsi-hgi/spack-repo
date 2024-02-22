# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigers(RPackage):
	"""Integration of Geography, Environment, and Remote Sensing

	Handling and manipulation polygons, coordinates, and other geographical objects. The tools include: polygon areas, barycentric and trilinear coordinates (Hormann and Floater, 2006, <doi:10.1145/1183287.1183295>), convex hull for polygons (Graham and Yao, 1983, <doi:10.1016/0196-6774(83)90013-5>), polygon triangulation (Toussaint, 1991, <doi:10.1007/BF01905693>), great circle and geodesic distances, Hausdorff distance, and reduced major axis.
	"""
	
	homepage = "https://github.com/emmanuelparadis/tigers"
	cran = "tigers" 

	version("0.1-3", md5="c09fbf7ad6bf495c2cd2ced0e8f0e643")

