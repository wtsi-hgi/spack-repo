# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdhererviz(RPackage):
	"""Adherence to Medications

	Interactive graphical user interface (GUI) for the package 
    'AdhereR', allowing the user to access different data sources, to explore 
    the patterns of medication use therein, and the computation of various  
    measures of adherence. It is implemented using Shiny and HTML/CSS/JavaScript. 
	"""
	
	homepage = "https://github.com/ddediu/AdhereR"
	cran = "AdhereRViz" 

	version("0.2.1", md5="4c857f45f4b557f3fe6f79da5427fe61")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-adherer@0.7.1:", type=("build", "run"))
	depends_on("r-data-table@1.9:", type=("build", "run"))
	depends_on("r-manipulate@1:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.4.4:", type=("build", "run"))
	depends_on("r-shinyjs@1:", type=("build", "run"))
	depends_on("r-v8@1.5:", type=("build", "run"))
	depends_on("r-colourpicker@1:", type=("build", "run"))
	depends_on("r-viridislite@0.3:", type=("build", "run"))
	depends_on("r-highlight@0.4:", type=("build", "run"))
	depends_on("r-clipr@0.4:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-rmariadb@1.0.5:", type=("build", "run"))
	depends_on("r-rsqlite@2.1:", type=("build", "run"))
