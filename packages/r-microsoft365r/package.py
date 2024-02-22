# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrosoft365r(RPackage):
	"""Interface to the 'Microsoft 365' Suite of Cloud Services

	An interface to the 'Microsoft 365' (formerly known as 'Office 365') suite of cloud services, building on the framework supplied by the 'AzureGraph' package. Enables access from R to data stored in 'Teams', 'SharePoint Online' and 'OneDrive', including the ability to list drive folder contents, upload and download files, send messages, and retrieve data lists. Also provides a full-featured 'Outlook' email client, with the ability to send emails and manage emails and mail folders.
	"""
	
	homepage = "https://github.com/Azure/Microsoft365R"
	cran = "Microsoft365R" 

	version("2.4.0", md5="bf23948ed2043a3f0099eff9745b643f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azureauth", type=("build", "run"))
	depends_on("r-azuregraph@1.3.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
