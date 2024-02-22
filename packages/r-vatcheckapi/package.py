# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVatcheckapi(RPackage):
	"""Client for the 'vatcheckapi.com' VAT Validation API

	An R client for the 'vatcheckapi.com' VAT number validation API. The API requires registration of an API key. Basic features are free, some require a paid subscription. You can find the full API documentation at <https://vatcheckapi.com/docs> .
	"""
	
	homepage = "https://vatcheckapi.com"
	cran = "vatcheckapi" 

	version("0.1.0", md5="83f027a065c1565b7c8ce328628d3451")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
