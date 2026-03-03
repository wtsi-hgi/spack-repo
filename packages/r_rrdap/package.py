# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrdap(RPackage):
	"""RDAP Server Querying

	Queries data from RDAP servers.
	"""
	
	cran = "Rrdap" 

	version("1.0.7", md5="2d46995904e22186b5572cce7b857e0d")
	version("1.0.6", md5="40eee25c6e525d8e8ec4661ca684b471")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
