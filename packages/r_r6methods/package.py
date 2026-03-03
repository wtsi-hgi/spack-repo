# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR6methods(RPackage):
	"""Make Methods for R6 Classes

	Generate boilerplate code for R6 classes. Given R6 class create getters 
    and/or setters for selected class fields or use RStudio addins to insert methods 
    straight into class definition.
	"""
	
	homepage = "https://github.com/jakubsob/r6methods"
	cran = "r6methods" 

	version("0.1.0", md5="b06e9eded4ace218d887beacaeddad62")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
