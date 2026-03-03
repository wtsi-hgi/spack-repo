# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplotgui(RPackage):
	"""Create Ggplots via a Graphical User Interface

	Easily explore data by creating ggplots through a (shiny-)GUI. R-code to recreate graph provided.   
	"""
	
	homepage = "https://github.com/gertstulp/ggplotgui/"
	cran = "ggplotgui" 

	version("1.0.0", md5="3c7327190dad1cdf222ae4684c22f237")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
