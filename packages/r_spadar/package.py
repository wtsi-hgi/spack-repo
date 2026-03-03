# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpadar(RPackage):
	"""Spherical Projections of Astronomical Data

	Provides easy to use functions to create all-sky grid plots of widely used astronomical coordinate systems (equatorial, ecliptic, galactic) and scatter plots of data on any of these systems including on-the-fly system conversion. It supports any type of spherical projection to the plane defined by the 'mapproj' package.
	"""
	
	cran = "SPADAR" 

	version("1.0", md5="b02e86a531fe158e8728ba2c94b8ed67")

	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-rceim", type=("build", "run"))
