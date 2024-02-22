# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgdax(RPackage):
	"""Wrapper for 'Coinbase Pro (erstwhile GDAX)' Cryptocurrency
Exchange

	Allow access to both public and private end points to Coinbase Pro (erstwhile GDAX) 
    cryptocurrency exchange. For authenticated flow, users must have valid api, secret and passphrase to be able to connect.
	"""
	
	homepage = "https://github.com/DheerajAgarwal/rgdax/"
	cran = "rgdax" 

	version("1.2.1", md5="c20f2c5cc77e77d6dede4343b161db86")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
