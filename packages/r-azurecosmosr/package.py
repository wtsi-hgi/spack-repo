# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurecosmosr(RPackage):
	"""Interface to the 'Azure Cosmos DB' 'NoSQL' Database Service

	An interface to 'Azure CosmosDB': <https://azure.microsoft.com/en-us/services/cosmos-db/>. On the admin side, 'AzureCosmosR' provides functionality to create and manage 'Cosmos DB' instances in Microsoft's 'Azure' cloud. On the client side, it provides an interface to the 'Cosmos DB' SQL API, letting the user store and query documents and attachments in 'Cosmos DB'. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureCosmosR"
	cran = "AzureCosmosR" 

	version("1.0.0", md5="b2f807d313d26f4fd3c1bf3cb888c677")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azurermr@2.3.3:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
