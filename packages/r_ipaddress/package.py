# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpaddress(RPackage):
	"""Data Analysis for IP Addresses and Networks

	Classes and functions for working with IP (Internet Protocol)
    addresses and networks, inspired by the Python 'ipaddress' module.
    Offers full support for both IPv4 and IPv6 (Internet Protocol versions
    4 and 6) address spaces. It is specifically designed to work well with
    the 'tidyverse'.
	"""
	
	homepage = "https://davidchall.github.io/ipaddress/"
	cran = "ipaddress" 

	version("1.0.2", md5="54fee6888b9297fc69bd72c3ef4a5e1b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@1.0.3:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-asioheaders", type=("build", "run"))
