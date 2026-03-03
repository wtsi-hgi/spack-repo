# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzureauth(RPackage):
	"""Authentication Services for Azure Active Directory

	Provides Azure Active Directory (AAD) authentication functionality for R users of Microsoft's 'Azure' cloud <https://azure.microsoft.com/>. Use this package to obtain 'OAuth' 2.0 tokens for services including Azure Resource Manager, Azure Storage and others. It supports both AAD v1.0 and v2.0, as well as multiple authentication methods, including device code and resource owner grant. Tokens are cached in a user-specific directory obtained using the 'rappdirs' package. The interface is based on the 'OAuth' framework in the 'httr' package, but customised and streamlined for Azure. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureAuth"
	cran = "AzureAuth" 

	version("1.3.3", md5="fd3b2870793d2a6e6c7df7db84400d41")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
