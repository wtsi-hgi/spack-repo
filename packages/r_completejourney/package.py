# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompletejourney(RPackage):
	"""Retail Shopping Data

	Retail shopping transactions for 2,469 households over one year.
    Originates from the 84.51° Complete Journey 2.0 source files 
    <https://www.8451.com/area51> which also includes useful metadata on 
    products, coupons, campaigns, and promotions.
	"""
	
	homepage = "https://github.com/bradleyboehmke/completejourney"
	cran = "completejourney" 

	version("1.1.0", md5="5d55b9aca5de06cf869ec6d083ff9103")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
