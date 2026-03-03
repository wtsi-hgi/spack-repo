# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhereport(RPackage):
	"""Geolocalization of IATA Codes

	Retrieve geographical information for airports using their IATA or ICAO codes.
	"""
	
	cran = "whereport" 

	version("0.1", md5="f4831782df5545d957c780909868a272")

	depends_on("r@3.4.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
