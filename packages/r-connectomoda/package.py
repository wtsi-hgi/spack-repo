# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnectomoda(RPackage):
	"""Download Data from Moda

	Connect to WFP's Moda platform to R, download data, and obtain the list of individuals with access to the project along with their access level.
	"""
	
	cran = "connectoModa" 

	version("1.0.0", md5="b3eb88ab0111d9d6990be08c73b67e52")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
