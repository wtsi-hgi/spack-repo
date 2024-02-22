# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurestor(RPackage):
	"""Storage Management in 'Azure'

	Manage storage in Microsoft's 'Azure' cloud: <https://azure.microsoft.com/en-us/product-categories/storage/>. On the admin side, 'AzureStor' includes features to create, modify and delete storage accounts. On the client side, it includes an interface to blob storage, file storage, and 'Azure Data Lake Storage Gen2': upload and download files and blobs; list containers and files/blobs; create containers; and so on. Authenticated access to storage is supported, via either a shared access key or a shared access signature (SAS). Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureStor"
	cran = "AzureStor" 

	version("3.7.0", md5="a2ad6c37daefbc693f656b0213341ee5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-azurermr@2.3:", type=("build", "run"))
