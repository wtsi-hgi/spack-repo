# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortrisk(RPackage):
	"""Portfolio Risk Analysis

	Risk Attribution of a portfolio with Volatility Risk Analysis.
	"""
	
	cran = "PortRisk" 

	version("1.1.0", md5="087354dbd606386c0f8324c29ddbe119")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
