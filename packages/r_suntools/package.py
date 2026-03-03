# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuntools(RPackage):
	"""Calculate Sun Position, Sunrise, Sunset, Solar Noon and Twilight

	Provides a set of convenient functions for calculating sun-related information, including the sun's position (elevation and azimuth), and the times of sunrise, sunset, solar noon, and twilight for any given geographical location on Earth. These calculations are based on equations provided by the National Oceanic & Atmospheric Administration (NOAA) <https://gml.noaa.gov/grad/solcalc/calcdetails.html> as described in "Astronomical Algorithms" by Jean Meeus (1991, ISBN: 978-0-943396-35-4). A resource for researchers and professionals working in fields such as climatology, biology, and renewable energy.
	"""
	
	homepage = "https://github.com/adokter/suntools/"
	cran = "suntools" 

	version("1.0.0", md5="9e2f93d4afaea50306f131e8975d1dc7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
