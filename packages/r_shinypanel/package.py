# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinypanel(RPackage):
	"""Shiny Control Panel

	Add shiny inputs with one or more inline buttons that grow and shrink with inputs. 
 Also add tool tips to input buttons and styling and messages for input validation.
	"""
	
	cran = "shinypanel" 

	version("0.1.5", md5="bcfd67cd6699bd82677c3b637dcb3087")

	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
