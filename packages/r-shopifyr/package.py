# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShopifyr(RPackage):
	"""An R Interface to the Shopify API

	An interface to the Admin API of the E-commerce service Shopify,
    (<https://help.shopify.com/en/api/reference>).
	"""
	
	homepage = "https://github.com/charliebone/shopifyr/"
	cran = "shopifyr" 

	version("1.0.0", md5="8406c4b27f8329b3932c9dca4e8d7503")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
