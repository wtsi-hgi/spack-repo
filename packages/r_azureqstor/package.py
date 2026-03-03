# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzureqstor(RPackage):
	"""Interface to 'Azure Queue Storage'

	An interface to 'Azure Queue Storage'. This is a cloud service for storing large numbers of messages, for example from automated sensors, that can be accessed remotely via authenticated calls using HTTP or HTTPS. Queue storage is often used to create a backlog of work to process asynchronously. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureQstor"
	cran = "AzureQstor" 

	version("1.0.1", md5="82ea33f390ece5e067b8c9a7b74ec205")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azurermr@2:", type=("build", "run"))
	depends_on("r-azurestor@3:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
