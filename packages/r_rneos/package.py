# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRneos(RPackage):
	"""XML-RPC Interface to NEOS

	Within this package the XML-RPC API to NEOS <https://neos-server.org/neos/> is implemented. This enables the user to pass optimization problems to NEOS and retrieve results within R.
	"""
	
	cran = "rneos" 

	version("0.4-0", md5="e801fbe5b0194a78311c31aeab4aae2f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
