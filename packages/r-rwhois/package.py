# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwhois(RPackage):
	"""WHOIS Server Querying

	Queries data from WHOIS servers.
	"""
	
	cran = "Rwhois" 

	version("1.0.16", md5="7e475ff56cb23b54d621965903309a45")
	version("1.0.14", md5="cc752d1525aa2d3b175a38b3a6b82bfd")

	depends_on("r-stringr", type=("build", "run"))
