# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThermindex(RPackage):
	"""Calculate Thermal Indexes

	Calculates several thermal comfort indexes using temperature, wind speed and relative humidity values, calculating indexes such as Humidex, windchill, Discomfort Index and others.
	"""
	
	cran = "ThermIndex" 

	version("0.2.0", md5="e21d7f7498746c3ff0c894d3ebe02526")

