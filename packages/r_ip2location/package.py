# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIp2location(RPackage):
	"""Lookup for IP Address Information

	Enables the user to find the country, region, district, city, coordinates, zip code, time zone, ISP, domain name, connection type, area code, weather, Mobile Country Code, Mobile Network Code, mobile brand name, elevation, usage type, address type, IAB category and Autonomous system information that any IP address or hostname originates from. Supported IPv4 and IPv6.
        Please visit <https://www.ip2location.com> to learn more. You may also want to visit <https://lite.ip2location.com> for free database download.
        This package requires 'IP2Location Python' module. At the terminal, please run 'pip install IP2Location' to install the module.
	"""
	
	homepage = "https://github.com/ip2location/ip2location-r"
	cran = "ip2location" 

	version("8.1.3", md5="722c952c6273ed8f00c3a104ed2f0027")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-reticulate@1.13:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-maps@3.4.1:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
