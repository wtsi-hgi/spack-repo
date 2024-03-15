# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIp(RPackage):
	"""Classes and Methods for 'IP' Addresses

	Provides S4 classes for Internet Protocol (IP) versions 4 and 6 addresses and efficient methods for 'IP' addresses comparison, arithmetic, bit manipulation and lookup. Both 'IPv4' and 'IPv6' arbitrary ranges are also supported as well as internationalized (IDN) domain lookup with and 'whois' query.
	"""
	
	cran = "IP" 

	version("0.1.3", md5="31d3a4bb2ecd792a439ea736d28b482c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("libidn2", type=("build", "link", "run"))
