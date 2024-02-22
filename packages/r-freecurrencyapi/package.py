# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreecurrencyapi(RPackage):
	"""Client for the 'freecurrencyapi.com' Currency Conversion API

	An R client for the 'freecurrencyapi.com' currency conversion API. The API requires registration of an API key. You can find the full API documentation at <https://freecurrencyapi.com/docs> .
	"""
	
	homepage = "https://freecurrencyapi.com"
	cran = "freecurrencyapi" 

	version("0.1.0", md5="0e6b18a240cba8b274479e51ea6eba91")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
