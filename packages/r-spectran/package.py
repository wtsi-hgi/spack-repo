# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectran(RPackage):
	"""Visual and Non-Visual Spectral Analysis of Light

	
 Analyse light spectra for visual and non-visual (often called
 melanopic) needs, wrapped up in a Shiny App. 'Spectran' allows for the import
 of spectra in various CSV forms but also provides a wide range of example
 spectra and even the creation of own spectral power distributions. The goal of
 the app is to provide easy access and a visual overview of the spectral
 calculations underlying common parameters used in the field. It is thus ideal
 for educational purposes or the creation of presentation ready graphs in
 lighting research and application. 'Spectran' uses equations and action spectra
 described in CIE S026 (2018) <doi:10.25039/S026.2018>, DIN/TS 5031-100 (2021)
 <doi:10.31030/3287213>, and ISO/CIE 23539 (2023)
 <doi:10.25039/IS0.CIE.23539.2023>.
	"""
	
	homepage = "https://github.com/LiTGde/Spectran"
	cran = "Spectran" 

	version("1.0.3", md5="a3ec57f63faf58a1273f5d224a151e3b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-chromote", type=("build", "run"))
	depends_on("r-colorspec", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gghighlight", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pagedown", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-spacesxyz", type=("build", "run"))
	depends_on("r-spscomps", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
