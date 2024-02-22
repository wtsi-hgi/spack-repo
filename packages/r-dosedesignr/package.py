# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDosedesignr(RPackage):
	"""Interactive Designing of Dose Finding Studies

	Provides the user with an interactive application which can be used to facilitate the planning of dose finding studies by applying the theory of optimal experimental design. 
	"""
	
	cran = "dosedesignR" 

	version("0.3.0", md5="7f0b99d762f4f93e150426de78fe6fff")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
