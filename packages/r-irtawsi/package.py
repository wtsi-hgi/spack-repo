# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtawsi(RPackage):
	"""Items Response Theory Analysis with Steps and Interpretation

	Analysis of Dichotomous and polytomous data using unidimensional Item Response Theory model (Chalmers (2012) <doi:10.18637/jss.v048.i06>) with user friendly Graphical User Interface. Suitable for  beginners who are learning Item Response Theory.
	"""
	
	cran = "irtawsi" 

	version("0.3.4", md5="8d5486ac8e104d320a15543cc02a6544")

	depends_on("r-dt", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bs4dash", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
