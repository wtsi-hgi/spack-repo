# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurevm(RPackage):
	"""Virtual Machines in 'Azure'

	Functionality for working with virtual machines (VMs) in Microsoft's 'Azure' cloud: <https://azure.microsoft.com/en-us/services/virtual-machines/>. Includes facilities to deploy, startup, shutdown, and cleanly delete VMs and VM clusters. Deployment configurations can be highly customised, and can make use of existing resources as well as creating new ones. A selection of predefined configurations is provided to allow easy deployment of commonly used Linux and Windows images, including Data Science Virtual Machines. With a running VM, execute scripts and install optional extensions. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureVM"
	cran = "AzureVM" 

	version("2.2.2", md5="a72a26da5a8752a34b8ab7de12bc045f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-azurermr@2.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
