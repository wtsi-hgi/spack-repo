# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGellipsoid(RPackage):
	"""Generalized Ellipsoids

	Represents generalized geometric ellipsoids with the "(U,D)" representation. It allows degenerate
	and/or unbounded ellipsoids, together with methods for linear and duality transformations, and for plotting.
	Thus ellipsoids are naturally extended to include lines, hyperplanes, points, cylinders, etc.
	This permits exploration of a variety to statistical issues that can be visualized using ellipsoids
	as discussed by Friendly, Fox & Monette (2013), Elliptical Insights: Understanding Statistical Methods 
	Through Elliptical Geometry <doi:10.1214/12-STS402>.
	"""
	
	homepage = "https://github.com/friendly/gellipsoid"
	cran = "gellipsoid" 

	version("0.7.3", md5="fff33ebc7e122e4420c6088544edc9bf")

	depends_on("r-rgl", type=("build", "run"))
