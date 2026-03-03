# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurevmmetadata(RPackage):
	"""Interface to Azure Virtual Machine Instance Metadata

	A simple interface to the instance metadata for a virtual machine running in Microsoft's 'Azure' cloud. This provides information about the VM's configuration, such as its processors, memory, networking, storage, and so on. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureVMmetadata"
	cran = "AzureVMmetadata" 

	version("1.0.1", md5="0bfe9f1b0b9a73d0c30f612757ab585a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
