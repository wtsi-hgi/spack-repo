# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinynotes(RPackage):
	"""Shiny Module for Taking Free-Form Notes

	An enterprise-targeted scalable and customizable 'shiny' module providing an easy way to incorporate free-form note taking or discussion boards into applications.
    The package includes a 'shiny' module that can be included in any 'shiny' application to create a panel containing searchable, editable text broken down by section headers.
    Can be used with a local 'SQLite' database, or a compatible remote database of choice.
	"""
	
	homepage = "https://github.com/danielkovtun/shinyNotes"
	cran = "shinyNotes" 

	version("0.0.2", md5="eadf6ea45e6cdf09477efdeb2bc6cc44")

	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
