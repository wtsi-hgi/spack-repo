# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPandora(RPackage):
	"""Retrieve Data using the API of the 'Pandora' Data Platform

	API wrapper that contains functions to retrieve data from the 'Pandora' databases. Web services for API: <https://pandora.earth/>. 
	"""
	
	homepage = "https://github.com/Pandora-IsoMemo/pandora-data"
	cran = "Pandora" 

	version("24.2.0", md5="a8e82706a5ebe69654a6027a66d9dfaa")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readods", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
