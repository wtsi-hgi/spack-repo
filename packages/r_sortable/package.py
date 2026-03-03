# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSortable(RPackage):
	"""Drag-and-Drop in 'shiny' Apps with 'SortableJS'

	Enables drag-and-drop behaviour in Shiny apps, by exposing the 
    functionality of the 'SortableJS' <https://sortablejs.github.io/Sortable/> 
    JavaScript library as an 'htmlwidget'. 
    You can use this in Shiny apps and widgets, 'learnr' tutorials as well as 
    R Markdown. In addition, provides a custom 'learnr' question type - 
    'question_rank()' - that allows ranking questions with drag-and-drop.
	"""
	
	homepage = "https://rstudio.github.io/sortable/"
	cran = "sortable" 

	version("0.5.0", md5="781f22fd8bf6652e42405c7c2c4a7520")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-learnr@0.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
