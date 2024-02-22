# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurermr(RPackage):
	"""Interface to 'Azure Resource Manager'

	A lightweight but powerful R interface to the 'Azure Resource Manager' REST API. The package exposes a comprehensive class framework and related tools for creating, updating and deleting 'Azure' resource groups, resources and templates. While 'AzureRMR' can be used to manage any 'Azure' service, it can also be extended by other packages to provide extra functionality for specific services. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureRMR"
	cran = "AzureRMR" 

	version("2.4.4", md5="ad56a32113e8025db6636e646b2af49d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azuregraph@1.2:", type=("build", "run"))
	depends_on("r-azureauth@1.2.1:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
