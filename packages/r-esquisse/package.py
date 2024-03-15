# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsquisse(RPackage):
	"""Explore and Visualize Your Data Interactively

	A 'shiny' gadget to create 'ggplot2' figures interactively with drag-and-drop to map your variables to different aesthetics.
    You can quickly visualize your data accordingly to their type, export in various formats,
    and retrieve the code to reproduce the plot.
	"""
	
	homepage = "https://dreamrs.github.io/esquisse/"
	cran = "esquisse" 

	version("1.2.0", md5="cbb0b4a1619bb2ae35f4fcdb417287e6")

	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-datamods@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-htmltools@0.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-phosphoricons", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinywidgets@0.6:", type=("build", "run"))
