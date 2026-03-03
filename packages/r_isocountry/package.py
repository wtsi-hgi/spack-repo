# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocountry(RPackage):
	"""ISO 3166-1 Country Codes

	ISO 3166-1 country codes provided by the International
    Organization for Standardization.
	"""
	
	homepage = "https://m-muecke.github.io/isocountry/"
	cran = "isocountry" 

	version("0.1.0", md5="48e7d12911432cb0b59380db3efe61f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
