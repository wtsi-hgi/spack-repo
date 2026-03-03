# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceconindex(RPackage):
	"""Price and Quantity Indices

	Tools for calculating Laspeyres, Paasche, and Fisher
  price and quantity indices.
	"""
	
	homepage = "http://www.micEcon.org"
	cran = "micEconIndex" 

	version("0.1-8", md5="39e980d7fb9ba917c0011797178352a1")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-misctools@0.6.1:", type=("build", "run"))
