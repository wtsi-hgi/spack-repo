# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbsodatar(RPackage):
	"""Statistics Netherlands (CBS) Open Data API Client

	The data and meta data from Statistics
    Netherlands (<https://www.cbs.nl>) can be browsed and downloaded. The client uses
    the open data API of Statistics Netherlands.
	"""
	
	homepage = "https://github.com/edwindj/cbsodataR"
	cran = "cbsodataR" 

	version("1.0.1", md5="7f2c6b68d97fe760e2aae0118c8d3fe1")

	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
