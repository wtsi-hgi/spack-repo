# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenbanker(RPackage):
	"""R Client for Querying the UK 'Open Banking' ('Open Data') API

	Creates a client with queries for the UK 'Open Banking' ('Open Data') API.
	"""
	
	homepage = "https://github.com/nik01010/openbankeR"
	cran = "openbankeR" 

	version("0.1.1", md5="7482db8bbe529069d7418f86d6214fa2")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httpcode", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
