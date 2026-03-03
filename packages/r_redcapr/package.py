# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedcapr(RPackage):
	"""Interaction Between R and REDCap

	Encapsulates functions to streamline calls from R to the REDCap
    API.  REDCap (Research Electronic Data CAPture) is a web application for
    building and managing online surveys and databases developed at Vanderbilt
    University.  The Application Programming Interface (API) offers an avenue
    to access and modify data programmatically, improving the capacity for
    literate and reproducible programming.
	"""
	
	homepage = "https://ouhscbbmc.github.io/REDCapR/"
	cran = "REDCapR" 

	version("1.1.0", md5="c2a60b7cb1b38525811c07210a745cc7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
