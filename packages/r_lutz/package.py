# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLutz(RPackage):
	"""Look Up Time Zones of Point Coordinates

	Input latitude and longitude values or an 'sf/sfc' POINT 
    object and get back the time zone in which they exist. Two methods are implemented. 
    One is very fast and uses 'Rcpp' in conjunction with data from the 'Javascript' library
    (<https://github.com/darkskyapp/tz-lookup-oss/>). This method also works outside of countries' 
    borders and in international waters, however speed comes at the cost of accuracy - near time 
    zone borders away from populated centres there is a chance that it will return the incorrect
    time zone. The other method is slower but more accurate - it uses the 'sf' package to intersect 
    points with a detailed map of time zones from here: 
    <https://github.com/evansiroky/timezone-boundary-builder/>. The package also 
    contains several utility functions for helping to understand and visualize 
    time zones, such as listing of world time zones, including information about 
    daylight savings times and their offsets from UTC. You can also plot a 
    time zone to visualize the UTC offset over a year and when daylight savings 
    times are in effect.
	"""
	
	homepage = "https://andyteucher.ca/lutz/"
	cran = "lutz" 

	version("0.3.2", md5="d7dff7617ad74a4b21efbbfbf5e73eeb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
