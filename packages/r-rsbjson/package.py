# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsbjson(RPackage):
	"""Handle R Requests from R Service Bus Applications with JSON
Payloads

	Package to Handle R Requests from R Service Bus Applications with JSON Payloads in a generic way.
    The incoming request is encoded as a string (character vector of length one) containing 
    the JSON file passed through by the client. 
	"""
	
	homepage = "https://www.rservicebus.io"
	cran = "RSBJson" 

	version("1.1.2", md5="1bbe1ed0d2e99793d480c1c30e592808")

	depends_on("r-jsonlite", type=("build", "run"))
