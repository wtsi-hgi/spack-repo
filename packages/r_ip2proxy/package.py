# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIp2proxy(RPackage):
	"""Lookup for IP Address Proxy Information

	Enable user to find the IP addresses which are used as VPN anonymizer, open proxies, web proxies and Tor exits.
    The package lookup the proxy IP address from IP2Proxy BIN Data file. You may visit <https://lite.ip2location.com> for free database download. 
	"""
	
	cran = "ip2proxy" 

	version("1.2.0", md5="d94011b591fdcc5c74266c0d960f786a")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-reticulate@1.13:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-maps@3.4.1:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
