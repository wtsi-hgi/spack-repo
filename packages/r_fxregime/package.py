# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFxregime(RPackage):
	"""Exchange Rate Regime Analysis

	Exchange rate regression and structural change tools
             for estimating, testing, dating, and monitoring
	     (de facto) exchange rate regimes.
	"""
	
	cran = "fxregime" 

	version("1.0-4", md5="af7c5a0bd60b373a10fe29788b3813b1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
