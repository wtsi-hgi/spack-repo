# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedamor(RPackage):
	"""Relational Data Modeler

	The aim of this package is to manipulate relational
   data models in R.
   It provides functions to create, modify and export data models
   in json format.
   It also allows importing models created
   with 'MySQL Workbench' (<https://www.mysql.com/products/workbench/>).
   These functions are accessible through a graphical user
   interface made with 'shiny'.
   Constraints such as types, keys, uniqueness and mandatory fields are
   automatically checked and corrected when editing a model.
   Finally, real data can be confronted to a model to check their compatibility.
	"""
	
	homepage = "https://patzaw.github.io/ReDaMoR/"
	cran = "ReDaMoR" 

	version("0.7.4", md5="8c2102cce29e7412b3edbc3b0039f886")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
