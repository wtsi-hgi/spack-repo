# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapiclient(RPackage):
	"""Dynamic OpenAPI/Swagger Client

	Access services specified in OpenAPI (formerly Swagger) format.
  It is not a code generator. Client is generated dynamically as a list of R 
  functions.
	"""
	
	homepage = "https://github.com/bergant/rapiclient"
	cran = "rapiclient" 

	version("0.1.3", md5="539efbcb49597feadc93f10d86606e2a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
