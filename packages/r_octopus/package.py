# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROctopus(RPackage):
	"""A Database Management Tool

	A database management tool built as a 'shiny' application. Connect to various 
    databases to send queries, upload files, preview tables, and more. 
	"""
	
	homepage = "https://github.com/MCodrescu/octopus"
	cran = "octopus" 

	version("0.4.2", md5="0a86f8e0f4cff6c0a9cdcb0fdd22785d")

	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
