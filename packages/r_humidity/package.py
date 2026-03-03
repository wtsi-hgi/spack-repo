# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumidity(RPackage):
	"""Calculate Water Vapor Measures from Temperature and Dew Point

	Vapor pressure, relative humidity, absolute humidity, specific humidity, and mixing ratio are commonly used water vapor measures in meteorology. This R package provides functions for calculating saturation vapor pressure (hPa), partial water vapor pressure (Pa), relative humidity (%), absolute humidity (kg/m^3), specific humidity (kg/kg), and mixing ratio (kg/kg) from temperature (K) and dew point (K). Conversion functions between humidity measures are also provided.
	"""
	
	homepage = "https://github.com/caijun/humidity"
	cran = "humidity" 

	version("0.1.5", md5="dec0bdf1563d874a62cb1025283cf3a8")

	depends_on("r@2.10:", type=("build", "run"))
