# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdaisi(RPackage):
	"""R Client for the Daisi Microservice Platform

	Connect, execute, and parse results from the Daisi Microservice Platform <https://www.daisi.io/>. The rdaisi client
  includes a set of functionality that allows remote execution of microservices directly from R.
  Daisis allow R users to access a wide variety of Python functionality and interact with them natively.
	"""
	
	homepage = "https://www.daisi.io/"
	cran = "rdaisi" 

	version("0.1.3", md5="a9546e6c22fc51e2b2e92c0a9b168dda")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
