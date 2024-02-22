# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmlrpc2(RPackage):
	"""Implementation of the Remote Procedure Call Protocol ('XML-RPC')

	The 'XML-RPC' is a remote procedure call protocol 
    based on 'XML'. The 'xmlrpc2' package is inspired by the 'XMLRPC'
	package but uses the 'curl' and 'xml2' packages instead 'RCurl' and 'XML'.
	"""
	
	cran = "xmlrpc2" 

	version("1.1", md5="7a8accbd8156a028b239967c35286435", url="https://cran.r-project.org/src/contrib/xmlrpc2_1.1.tar.gz")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
