# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurecognitive(RPackage):
	"""Interface to Azure Cognitive Services

	An interface to Azure Cognitive Services <https://docs.microsoft.com/en-us/azure/cognitive-services/>. Both an 'Azure Resource Manager' interface, for deploying Cognitive Services resources, and a client framework are supplied. While 'AzureCognitive' can be called by the end-user, it is meant to provide a foundation for other packages that will support specific services, like Computer Vision, Custom Vision, language translation, and so on. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureCognitive"
	cran = "AzureCognitive" 

	version("1.0.1", md5="ca0749f0fcc52e9dfa1a533ff63da016")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azureauth@1.2:", type=("build", "run"))
	depends_on("r-azurermr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
