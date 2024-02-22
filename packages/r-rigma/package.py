# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRigma(RPackage):
	"""Access to the 'Figma' API

	The goal of Rigma is to provide a user friendly client to the 'Figma'
 API <https://www.figma.com/developers/api>. It uses the latest `httr2` for a 
 stable interface with the REST API. More than 20 methods are provided to 
 interact with 'Figma' files, and teams. Get design data into R by reading 
 published components and styles, converting and downloading images, getting 
 access to the full 'Figma' file as a hierarchical data structure, and much 
 more. Enhance your creativity and streamline the application development by
 automating the extraction, transformation, and loading of design data to your 
 applications and 'HTML' documents.
	"""
	
	homepage = "https://github.com/AleKoure/Rigma"
	cran = "Rigma" 

	version("0.2.1", md5="9b64087e0d2325d83bda9feb04d86d53")

	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
