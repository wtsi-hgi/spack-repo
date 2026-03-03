# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestrserve(RPackage):
	"""A Framework for Building HTTP API

	
  Allows to easily create high-performance full featured HTTP APIs from R
  functions. Provides high-level classes such as 'Request', 'Response',
  'Application', 'Middleware' in order to streamline server side
  application development. Out of the box allows to serve requests using
  'Rserve' package, but flexible enough to integrate with other HTTP servers
  such as 'httpuv'.
	"""
	
	homepage = "https://restrserve.org"
	cran = "RestRserve" 

	version("1.2.1", md5="a457d6c706106447a98a192752aa1875")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rserve@1.7.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-uuid@0.1.2:", type=("build", "run"))
	depends_on("r-checkmate@1.9.4:", type=("build", "run"))
	depends_on("r-mime@0.7:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-digest@0.6.29:", type=("build", "run"))
