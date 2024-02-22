# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzuretablestor(RPackage):
	"""Interface to the Table Storage Service in 'Azure'

	An interface to the table storage service in 'Azure': <https://azure.microsoft.com/en-us/services/storage/tables/>. Supplies functionality for reading and writing data stored in tables, both as part of a storage account and from a 'CosmosDB' database with the table service API. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureTableStor"
	cran = "AzureTableStor" 

	version("1.0.0", md5="b3afeed7f53189b41bc8f66345628d11")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azurermr@2:", type=("build", "run"))
	depends_on("r-azurestor@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
