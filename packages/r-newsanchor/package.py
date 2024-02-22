# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNewsanchor(RPackage):
	"""Client for the News API

	Interface to gather news from the 'News API', based on a multilevel query <https://newsapi.org/>. A personal API key is required. 
	"""
	
	cran = "newsanchor" 

	version("0.1.1", md5="eaa375fdc2b9abcf3e4129ea53c02a05")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
