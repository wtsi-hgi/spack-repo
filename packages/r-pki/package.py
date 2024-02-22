# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPki(RPackage):
	"""Public Key Infrastucture for R Based on the X.509 Standard

	Public Key Infrastucture functions such as verifying certificates, RSA encription and signing which can be used to build PKI infrastructure and perform cryptographic tasks.
	"""
	
	homepage = "http://www.rforge.net/PKI"
	cran = "PKI" 

	version("0.1-12", md5="7d7d1b331cf07bee9ec8c9c97027ff40")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("openssl@1.0.2:", type=("build", "link", "run"))
