# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurecontainers(RPackage):
	"""Interface to 'Container Instances', 'Docker Registry' and
'Kubernetes' in 'Azure'

	An interface to container functionality in Microsoft's 'Azure' cloud: <https://azure.microsoft.com/en-us/product-categories/containers/>. Manage 'Azure Container Instance' (ACI), 'Azure Container Registry' (ACR) and 'Azure Kubernetes Service' (AKS) resources, push and pull images, and deploy services. On the client side, lightweight shells to the 'docker', 'docker-compose', 'kubectl' and 'helm' commandline tools are provided. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureContainers"
	cran = "AzureContainers" 

	version("1.3.2", md5="9599a167a2bbaf01297a67fb552aada7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-azurermr@2:", type=("build", "run"))
	depends_on("r-azuregraph@1.1:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
