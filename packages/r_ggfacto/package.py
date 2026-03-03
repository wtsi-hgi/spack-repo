# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfacto(RPackage):
	"""Graphs for Correspondence Analysis

	Readable, complete and pretty graphs for correspondence analysis made 
    with 'FactoMineR'. They can be rendered as interactive 'HTML' plots, showing useful
    informations at mouse hover. The interest is not mainly visual but statistical:
    it helps the reader to keep in mind the data contained in the cross-table or Burt
    table while reading the correspondence analysis, thus preventing over-interpretation.
    Most graphs are made with 'ggplot2', which means that you can use the + syntax to 
    manually add as many graphical pieces you want, or change theme elements. 3D 
    graphs are made with 'plotly'.
	"""
	
	homepage = "https://github.com/BriceNocenti/ggfacto"
	cran = "ggfacto" 

	version("0.3.0", md5="68c7e54454d3728ddd8e3aa6b63c59f6")
	version("0.2.3", md5="29fc116742423069058087780e040453")

	depends_on("r-factominer@2:", type=("build", "run"))
	depends_on("r-ggiraph@0.8.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-tabxplor@1.0.3:", type=("build", "run"))
	depends_on("r-withr@2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-ggforce@0.4:", type=("build", "run"))
