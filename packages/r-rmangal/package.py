# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmangal(RPackage):
	"""'Mangal' Client

	An interface to the 'Mangal' database - a collection of ecological networks. This package includes functions to work with the 'Mangal RESTful API' methods (<https://mangal-interactions.github.io/mangal-api/>).
	"""
	
	homepage = "https://docs.ropensci.org/rmangal/"
	cran = "rmangal" 

	version("2.1.3", md5="6b165de00dcf1568cbd74b5ea9a6288a")

	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-igraph@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
