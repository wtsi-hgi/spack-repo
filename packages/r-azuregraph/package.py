# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzuregraph(RPackage):
	"""Simple Interface to 'Microsoft Graph'

	A simple interface to the 'Microsoft Graph' API <https://learn.microsoft.com/en-us/graph/overview>. 'Graph' is a comprehensive framework for accessing data in various online Microsoft services. This package was originally intended to provide an R interface only to the 'Azure Active Directory' part, with a view to supporting interoperability of R and 'Azure': users, groups, registered apps and service principals. However it has since been expanded into a more general tool for interacting with Graph. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureGraph"
	cran = "AzureGraph" 

	version("1.3.4", md5="9ccfd80f0c994c927fcb8b30203ebe83")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azureauth@1.0.1:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
