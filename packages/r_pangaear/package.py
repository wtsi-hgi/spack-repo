# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPangaear(RPackage):
	"""Client for the 'Pangaea' Database

	Tools to interact with the 'Pangaea' Database
    (<https://www.pangaea.de>), including functions for searching for data,
    fetching 'datasets' by 'dataset' 'ID', and working with the 'Pangaea'
    'OAI-PMH' service.
	"""
	
	homepage = "https://github.com/ropensci/pangaear"
	cran = "pangaear" 

	version("1.1.0", md5="cacc6e555addf7de64745995d380b7c8")

	depends_on("r-crul@0.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-xml2@1.1.1:", type=("build", "run"))
	depends_on("r-oai@0.2.2:", type=("build", "run"))
	depends_on("r-tibble@1.1:", type=("build", "run"))
	depends_on("r-hoardr@0.2:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
