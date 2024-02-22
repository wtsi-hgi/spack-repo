# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurekeyvault(RPackage):
	"""Key and Secret Management in 'Azure'

	Manage keys, certificates, secrets, and storage accounts in Microsoft's 'Key Vault' service: <https://azure.microsoft.com/services/key-vault/>. Provides facilities to store and retrieve secrets, use keys to encrypt, decrypt, sign and verify data, and manage certificates. Integrates with the 'AzureAuth' package to enable authentication with a certificate, and with the 'openssl' package for importing and exporting cryptographic objects. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureKeyVault"
	cran = "AzureKeyVault" 

	version("1.0.5", md5="1f43e01f064955a1e419dcd9bb2218b7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-azurermr", type=("build", "run"))
	depends_on("r-azuregraph", type=("build", "run"))
	depends_on("r-azureauth@1.0.1:", type=("build", "run"))
