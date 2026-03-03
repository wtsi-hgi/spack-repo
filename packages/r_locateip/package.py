# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocateip(RPackage):
	"""Locate IP Addresses with 'ip-api'

	Download Internet Protocol (IP) address location and more from the 'ip-api' application programming interface (API) <https://ip-api.com/>. The package makes it easy to get the latitude, longitude, country, region, and organisation associated to the provided IP address. The information is conveniently returned in a rectangular format.
	"""
	
	cran = "locateip" 

	version("0.1.2", md5="5ad4c9ae596fcffac68006dfaa53e0de")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
