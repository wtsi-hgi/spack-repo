# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFresh(RPackage):
	"""Create Custom 'Bootstrap' Themes to Use in 'Shiny'

	Customize 'Bootstrap' and 'Bootswatch' themes, like colors, fonts, grid layout, 
  to use in 'Shiny' applications, 'rmarkdown' documents and 'flexdashboard'.
	"""
	
	homepage = "https://github.com/dreamRs/fresh"
	cran = "fresh" 

	version("0.2.0", md5="cf4795ab6aab4bebfa317d598ad3aa1e")

	depends_on("r-sass", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
