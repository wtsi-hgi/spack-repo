# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinysearchbar(RPackage):
	"""Shiny Searchbar - An Input Widget for Highlighting Text and More

	Add a searchbar widget to your 'Shiny' application. The widget
  quickly integrates with any existing element containing text to highlight
  matches. Highlighting is done with the 'JavaScript' library 'mark.js'. The
  widget includes buttons to cycle through multiple instances of the match and
  automatically scroll to the matches in an overflow element (or window). The
  widget also displays the total number of matches and which match is currently
  being cycled through. The widget is structured as a 'Bootstrap 3' input
  group.
	"""
	
	homepage = "https://github.com/jes-n/shiny-searchbar"
	cran = "shinySearchbar" 

	version("1.0.0", md5="1e847ace97b5f007d02ef9295f30d2ca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
