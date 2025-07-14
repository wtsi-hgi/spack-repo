# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpm(RPackage):
	"""Well Plate Maker

	The Well-Plate Maker (WPM) is a shiny application deployed as an R package. Functions for a command-line/script use are also available. The WPM allows users to generate well plate maps to carry out their experiments while improving the handling of batch effects. In particular, it helps controlling the "plate effect" thanks to its ability to randomize samples over multiple well plates. The algorithm for placing the samples is inspired by the backtracking algorithm: the samples are placed at random while respecting specific spatial constraints.
	"""
	
	homepage = "https://github.com/HelBor/wpm"
	bioc = "wpm"

	version("1.18.0", commit="9e957bbc0045026b9255cea40e8bf9669e812a78")
	version("1.12.0", commit="d3592db2a3ce5a2c3afcf649beac2a28a033d23c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
