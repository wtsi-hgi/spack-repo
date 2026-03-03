# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodosetools(RPackage):
	"""An R Shiny Application for Biological Dosimetry

	A tool to perform all different statistical tests and calculations
    needed by Biological Dosimetry Laboratories.
	"""
	
	homepage = "https://biodosetools-team.github.io/biodosetools/"
	cran = "biodosetools" 

	version("3.6.1", md5="6839542d16ca3988caece3f2422e33a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets@0.5:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
