# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyhttr(RPackage):
	"""Progress Bars for Downloads in 'shiny' Apps

	Modifies the progress() function from 'httr' package to let it 
      send output to progressBar() function from 'shinyWidgets' package. 
      It is just a tweak at the original functions from 'httr' package to 
      make it smooth for 'shiny' developers.
	"""
	
	homepage = "https://github.com/curso-r/shinyhttr"
	cran = "shinyhttr" 

	version("1.1.0", md5="8e9694127e624539fd8d9f9235ac57ba")

	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
