# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCryptoverse(RPackage):
	"""Visualization and Analytics for the Cryptoverse

	Providing data to quickly visualize and analyze data from several cryptocurrencies.
	"""
	
	cran = "cryptoverse" 

	version("0.1.0", md5="6758bb57987f11d58313240fda799729")

	depends_on("r@3.5:", type=("build", "run"))
