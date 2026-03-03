# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatserv(RPackage):
	"""'NatureServe' Interface

	Interface to 'NatureServe' (<https://www.natureserve.org/>).
    Includes methods to get data, image metadata, search taxonomic names,
    and make maps.
	"""
	
	homepage = "https://docs.ropensci.org/natserv"
	cran = "natserv" 

	version("1.0.0", md5="c7e7c716b0aba4d263dc4b289ade3d38")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-crul@0.7:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
