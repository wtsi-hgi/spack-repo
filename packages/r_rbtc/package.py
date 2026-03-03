# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbtc(RPackage):
	"""Bitcoin API

	Implementation of the RPC-JSON API for Bitcoin and utility functions for address creation and content analysis of the blockchain.
	"""
	
	cran = "rbtc" 

	version("0.1-6", md5="a333b86c69c00383f2c39c537890ed59")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
