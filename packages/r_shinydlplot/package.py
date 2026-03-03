# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinydlplot(RPackage):
	"""Add a Download Button to a 'shiny' Plot or 'plotly'

	Add a download button to a 'shiny' plot or 'plotly' that appears when
  the plot is hovered. A tooltip, styled to resemble 'plotly' buttons, is displayed 
  on hover of the download button. The download button can be used to allow users
  to download the dataset used for a plot.
	"""
	
	cran = "shinydlplot" 

	version("0.1.4", md5="2e1c976f052a10efa300323878988aa3")

	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
	depends_on("r-plotly@4.9.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5:", type=("build", "run"))
