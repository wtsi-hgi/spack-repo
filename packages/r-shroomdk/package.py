# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShroomdk(RPackage):
	"""Accessing the Flipside Crypto ShroomDK API

	Programmatic access to Flipside Crypto data via the Compass RPC API: <https://api-docs.flipsidecrypto.xyz/>. As simple as auto_paginate_query() but with core functions as needed for troubleshooting. Note, 0.1.1 support deprecated 2023-05-31.
	"""
	
	cran = "shroomDK" 

	version("0.3.0", md5="82afb1d31368f923c49b254b2b925f3a")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
