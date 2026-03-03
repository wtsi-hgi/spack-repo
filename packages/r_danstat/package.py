# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDanstat(RPackage):
	"""R Client for the Statistics Denmark Databank API

	The purpose of the package is to enable an R function interface into the Statistics Denmark Databank API mainly for research purposes. 
    The Statistics Denmark Databank API has four endpoints, see here for more information and testing the API in their console: <https://www.dst.dk/en/Statistik/brug-statistikken/muligheder-i-statistikbanken/api>.
    This package mimics the structure of the API and provides four main functions to match the functionality of the API endpoints.
	"""
	
	cran = "danstat" 

	version("0.2.0", md5="b683b02f9dc55f8b8403a43236782ea9")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
