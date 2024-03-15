# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcetool(RPackage):
	"""Efficient and Accessible Discrete Choice Experiments

	Design, conduct and analyze 'DCEs' from a virtual interface in shiny. Reference: Perez-Troncoso, D. (2022) <https://github.com/danielpereztr/DCEtool>.
	"""
	
	cran = "DCEtool" 

	version("1.1.0", md5="481402a3c82435531b3807892bb2d140")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-idefix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-adjustedcranlogs", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
