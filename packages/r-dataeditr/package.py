# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataeditr(RPackage):
	"""An Interactive Editor for Viewing, Entering, Filtering & Editing
Data

	An interactive editor built on 'rhandsontable' to allow the 
  interactive viewing, entering, filtering and editing of data in R 
  <https://dillonhammill.github.io/DataEditR/>.
	"""
	
	homepage = "https://github.com/DillonHammill/DataEditR"
	cran = "DataEditR" 

	version("0.1.5", md5="67eb7f5bb65cc0adb3d7062344d4bddd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-rhandsontable@0.3.8:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
