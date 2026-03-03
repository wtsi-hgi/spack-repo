# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscopus(RPackage):
	"""Scopus Database 'API' Interface

	Uses Elsevier 'Scopus' API
    <https://dev.elsevier.com/sc_apis.html> to download 
    information about authors and their citations.
	"""
	
	homepage = "https://dev.elsevier.com/sc_apis.html"
	cran = "rscopus" 

	version("0.6.6", md5="6c429b6cccd6620c9ac288d8a68d6ad9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
