# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurrencyapi(RPackage):
	"""Client for the 'currencyapi.com' Currency Conversion API

	An R client for the 'currencyapi.com' currency conversion API. The API requires registration of an API key. Basic features are free, some require a paid subscription. You can find the full API documentation at <https://currencyapi.com/docs> .
	"""
	
	homepage = "https://currencyapi.com"
	cran = "currencyapi" 

	version("0.1.0", md5="40795998830a2de213b2c910664864e0")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
