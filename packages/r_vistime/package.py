# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVistime(RPackage):
	"""Pretty Timelines in R

	A library for creating time based charts, like Gantt or timelines. Possible outputs 
  include 'ggplot2' diagrams, 'plotly.js' graphs, 'Highcharts.js' widgets and data.frames. Results can be
  used in the 'RStudio' viewer pane, in 'RMarkdown' documents or in Shiny apps. In the 
  interactive outputs created by vistime() and hc_vistime(), you can interact with the 
  plot using mouse hover or zoom.
	"""
	
	homepage = "https://shosaco.github.io/vistime/"
	cran = "vistime" 

	version("1.2.4", md5="2134200869be260e3cbbb03f89d182fe")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-plotly@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel@0.7:", type=("build", "run"))
	depends_on("r-rcolorbrewer@0.2.2:", type=("build", "run"))
