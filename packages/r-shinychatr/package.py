# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinychatr(RPackage):
	"""R Shiny Chat Module

	Provides an easy-to-use module for adding a chat to a Shiny app. Allows
    users to send messages and view messages from other users. 
    Messages can be stored in a database or a .rds file.
	"""
	
	homepage = "https://github.com/julianschmocker/shinyChatR"
	cran = "shinyChatR" 

	version("1.1.0", md5="065eb996fd578bf14ab4ae26be377df1")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
