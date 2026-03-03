# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurevision(RPackage):
	"""Interface to Azure Computer Vision Services

	An interface to 'Azure Computer Vision' <https://docs.microsoft.com/azure/cognitive-services/Computer-vision/Home> and 'Azure Custom Vision' <https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/home>, building on the low-level functionality provided by the 'AzureCognitive' package. These services allow users to leverage the cloud to carry out visual recognition tasks using advanced image processing models, without needing powerful hardware of their own. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureVision"
	cran = "AzureVision" 

	version("1.0.2", md5="64624070bbc28f16a856df90d058780a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azurermr", type=("build", "run"))
	depends_on("r-azurecognitive", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
