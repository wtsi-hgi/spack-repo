# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbch(RPackage):
	"""Extraction and Analysis of Data from the Bitcoin Cash (BCH)
Blockchain

	Issues RPC-JSON calls to 'bitcoind', the daemon of Bitcoin Cash (BCH), to
    extract transaction data from the blockchain. BCH is a fork of Bitcoin that permits
    a greater number of transactions per second. A BCH daemon is available under an MIT
    license from the Bitcoin Unlimited website <https://www.bitcoinunlimited.info>.
	"""
	
	homepage = "https://github.com/Rucknium/rbch"
	cran = "rbch" 

	version("0.1-1", md5="f10704518cf398ae4c7678abcf81d0af")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
