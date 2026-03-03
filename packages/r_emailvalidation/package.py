# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmailvalidation(RPackage):
	"""Client for the 'emailalvalidation.io' E-Mail Validation API

	An R client for the 'emailvalidation.io' e-mail verification API. The API requires registration of an API key. Basic features are free, some require a paid subscription. You can find the full API documentation at <https://emailvalidation.io/docs> .
	"""
	
	homepage = "https://emailvalidation.io"
	cran = "emailvalidation" 

	version("0.1.0", md5="1c632b2dd2e1b71c002bf3635e02e9d8")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
