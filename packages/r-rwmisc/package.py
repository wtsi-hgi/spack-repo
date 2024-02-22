# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwmisc(RPackage):
	"""Miscellaneous Spatial Functions

	Contains convenience functions for working with spatial data across
    multiple UTM zones, raster-vector operations common in the analysis of 
    conflict data, and converting degrees, minutes, and seconds latitude and
    longitude coordinates to decimal degrees.
	"""
	
	homepage = "https://github.com/jayrobwilliams/RWmisc"
	cran = "RWmisc" 

	version("0.1.2", md5="76bc55d300c64df074d8576445b36165")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
