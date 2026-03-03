# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiebanxicor(RPackage):
	"""Query Data Series from Bank of Mexico

	Allows to retrieve time series of all indicators available in the Bank of Mexico's Economic Information System (<http://www.banxico.org.mx/SieInternet/>).
	"""
	
	cran = "siebanxicor" 

	version("1.0.0", md5="e0d2b340908ef183b5fc0fb2e7dd0197")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
